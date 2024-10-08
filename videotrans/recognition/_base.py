import os
import re
from typing import List, Dict, Union

from videotrans.configure import config
from videotrans.configure._base import BaseCon

from videotrans.util import tools


class BaseRecogn(BaseCon):

    def __init__(self, detect_language=None, audio_file=None, cache_folder=None,
                 model_name=None, inst=None, uuid=None, is_cuda=None):
        super().__init__()
        # 需要判断当前是主界面任务还是单独任务，用于确定使用哪个字幕编辑区
        self.detect_language = detect_language
        self.audio_file = audio_file
        self.cache_folder = cache_folder
        self.model_name = model_name
        self.inst = inst
        self.uuid = uuid
        self.is_cuda = is_cuda
        self.has_done = False
        self.error = ''


        self.api_url = ''
        self.proxies = None

        self.flag = [
            ",",
            
            ".",
            "?",
            "!",
            ";",
           
            "，",
            "。",
            "？",
            "；",      
            "！"
        ]
        
        self.join_word_flag = " "
        
        self.jianfan=False
        if self.detect_language[:2].lower() in ['zh', 'ja', 'ko']:
            self.maxlen = int(config.settings['cjk_len'])
            self.jianfan = True if self.detect_language[:2] == 'zh' and config.settings['zh_hant_s'] else False
        else:
            self.maxlen = int(config.settings['other_len'])
        
        if not tools.vail_file(self.audio_file):
            raise Exception(f'[error]not exists {self.audio_file}')

    # 出错时发送停止信号
    def run(self) -> Union[List[Dict], None]:
        self._signal(text="")
        try:
            if self.detect_language[:2].lower() in ['zh', 'ja', 'ko']:
                self.flag.append(" ")
                self.join_word_flag = ""
            return self._exec()
        except Exception as e:
            config.logger.exception(e, exc_info=True)
            msg = f'{str(e)}'
            if re.search(r'cub[a-zA-Z0-9_.-]+?\.dll', msg, re.I | re.M) is not None:
                msg = f'【缺少cuBLAS.dll】请点击菜单栏-帮助/支持-下载cublasxx.dll,或者切换为openai模型 {msg} ' if config.defaulelang == 'zh' else f'[missing cublasxx.dll] Open menubar Help&Support->Download cuBLASxx.dll or use openai model {msg}'
            elif re.search(r'out\s+?of.*?memory', msg, re.I):
                msg = f'显存不足，请使用较小模型，比如 tiny/base/small {msg}' if config.defaulelang == 'zh' else f'Insufficient video memory, use a smaller model such as tiny/base/small {msg}'
            elif re.search(r'cudnn', msg, re.I):
                msg = f'cuDNN错误，请尝试升级显卡驱动，重新安装CUDA12.x和cuDNN9 {msg}' if config.defaulelang == 'zh' else f'cuDNN error, please try upgrading the graphics card driver and reinstalling CUDA12.x and cuDNN9 {msg}'
            self._signal(text=msg, type="error")
            raise
        finally:
            if self.shound_del:
                self._set_proxy(type='del')

    def _exec(self) -> Union[List[Dict], None]:
        pass

    
    
    def add_punctuation_to_words(self,data):
        import nltk,os
        # 指定 nltk 数据存放路径
        nltk.data.path.append(config.ROOT_DIR+"/models")

        # 下载 punkt_tab 资源到指定路径
        if not os.path.exists(config.ROOT_DIR+"/models/tokenizers/punkt_tab"):
            nltk.download('punkt_tab', download_dir=config.ROOT_DIR+"/models")


        """
        在字级别信息中插入标点符号。

        Args:
            data: openai-whisper 返回的字幕数据，包含字级别信息。

        Returns:
            添加标点符号后的字幕数据，格式与输入相同。
        """

        for segment in data:
            if "words" not in segment:
                continue

            text = "".join([word_info["word"] for word_info in segment["words"]])
            sentences = nltk.sent_tokenize(text)    # 使用 nltk 分句
            punctuated_text = ""
            for sentence in sentences:
                if sentence[-1] in [',','?','!','，','。','？','！']:
                    punctuated_text += sentence + " "
                else:
                    punctuated_text += sentence + ". "
            punctuated_text = punctuated_text.strip()

            # 将标点符号插入到对应的 word 中
            word_index = 0
            punc_index = 0
            new_words = []
            for word_info in segment["words"]:
                word = word_info["word"]
                while punc_index < len(punctuated_text) and punctuated_text[punc_index] in word:
                    punc_index += 1
                if punc_index < len(punctuated_text) and punctuated_text[punc_index] in [',','.','?','!','，','。','？','！']:
                    if punctuated_text[punc_index] not in word:
                        new_words.append({"word": word + punctuated_text[punc_index], "start": word_info["start"], "end": word_info["end"]})
                        punc_index += 1
                    else:
                        new_words.append(word_info)
                else:
                    new_words.append(word_info)

            segment["words"] = new_words
            segment["text"] = punctuated_text
            
        return data

    def re_segment_sentences(self,data,language=""):
        """
        根据字级别信息重新划分句子，考虑 word 中可能包含多个字符的情况，并优化断句逻辑。

        Args:
            data: openai-whisper 返回的字幕数据，包含字级别信息。

        Returns:
            重新划分后的字幕数据，格式与输入相同。
        """
        import zhconv
        try:
            data=self.add_punctuation_to_words(data)
        except Exception as e:
            config.logger.exception(e)
            print('使用nltk分句失败')
            
        new_data = []
        sentence = ""
        try:
            sentence_start = data[0]["words"][0]['start']
        except Exception as e:
            print(e)
        sentence_end = 0
        word_index = 0# 使用 word_index 跟踪当前字在 segment["words"] 中的位置
        
        flags=r"[，。？！,?!]"
        if self.detect_language[:2] in ['zh','ja','ko']:
            flags=r"[，。？！,?!\s]"
            maxlen=2
        else:        
            maxlen=10
        
        for segment in data:
            for i, word_info in enumerate(segment["words"]):
                word = word_info["word"]
                start = word_info["start"]
                end = word_info["end"]

                word=re.sub(r"(?<!\d)\.(?!\d)", ",", word)
                sentence += word
                sentence_end = end
                
                # 判断是否需要断句
                if len(sentence.strip())>maxlen and re.search(flags, word)  or \
                     (i + 1 < len(segment["words"]) and segment["words"][i+1]["start"] > end): # 判断下一个字的开始时间是否大于当前字的结束时间
                    if self.jianfan:
                        sentence=zhconv.convert(sentence, 'zh-hans')
                    tmp={
                            "line": len(new_data)+1,
                            "start_time": sentence_start,
                            "end_time": sentence_end,
                            "text": sentence.strip() if sentence[-1] not in ['.','。',','] else sentence[:-1].strip(),
                    }
                    tmp['time']=f'{tools.ms_to_time_string(ms=tmp["start_time"])} --> {tools.ms_to_time_string(ms=tmp["end_time"])}'
                    new_data.append(tmp)
                    
                    sentence = ""
                    sentence_start = segment["words"][i+1]["start"] if i + 1 < len(segment["words"]) else  end
                    word_index = i + 1# 更新 word_index                    
                # 句子时长超过 5s 断句
                elif sentence_end - sentence_start >= 4000:
                    if self.jianfan:
                        sentence=zhconv.convert(sentence, 'zh-hans')
                    tmp={
                            "line": len(new_data)+1,
                            "start_time": sentence_start,
                            "end_time": sentence_end,
                            "text": sentence.strip() if sentence[-1] not in ['.','。',','] else sentence[:-1].strip(),
                    }
                    new_data.append(tmp)
                    tmp['time']=f'{tools.ms_to_time_string(ms=tmp["start_time"])} --> {tools.ms_to_time_string(ms=tmp["end_time"])}'
                    sentence = ""
                    sentence_start = segment["words"][i+1]["start"] if i + 1 < len(segment["words"]) else  end
                    word_index = i + 1# 更新 word_index

        # 处理最后一句
        if sentence:
            if sentence_end - sentence_start > 0:
                if self.jianfan:
                    sentence=zhconv.convert(sentence, 'zh-hans')
                tmp={
                            "line": len(new_data)+1,
                            "start_time": sentence_start,
                            "end_time": sentence_end,
                            "text": sentence.strip() if sentence[-1] not in ['.','。',','] else sentence[:-1].strip(),
                    }
                tmp['time']=f'{tools.ms_to_time_string(ms=tmp["start_time"])} --> {tools.ms_to_time_string(ms=tmp["end_time"])}'
                new_data.append(tmp)

        return new_data
    


    # True 退出
    def _exit(self) -> bool:
        if config.exit_soft or (config.current_status != 'ing' and config.box_recogn != 'ing'):
            return True
        return False
