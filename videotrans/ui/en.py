# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'en.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 771)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.btn_get_video = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_video.sizePolicy().hasHeightForWidth())
        self.btn_get_video.setSizePolicy(sizePolicy)
        self.btn_get_video.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_get_video.setStyleSheet("")
        self.btn_get_video.setObjectName("btn_get_video")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_get_video)
        self.source_mp4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.source_mp4.setMinimumSize(QtCore.QSize(0, 35))
        self.source_mp4.setInputMask("")
        self.source_mp4.setText("")
        self.source_mp4.setObjectName("source_mp4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_mp4)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.btn_save_dir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save_dir.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_save_dir.setStyleSheet("")
        self.btn_save_dir.setObjectName("btn_save_dir")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_save_dir)
        self.target_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.target_dir.setMinimumSize(QtCore.QSize(0, 35))
        self.target_dir.setInputMask("")
        self.target_dir.setText("")
        self.target_dir.setObjectName("target_dir")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_dir)
        self.horizontalLayout_6.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 35))
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.translate_type = QtWidgets.QComboBox(self.layoutWidget)
        self.translate_type.setMinimumSize(QtCore.QSize(0, 35))
        self.translate_type.setObjectName("translate_type")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.translate_type)
        self.horizontalLayout_5.addLayout(self.formLayout_3)
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.proxy = QtWidgets.QLineEdit(self.layoutWidget)
        self.proxy.setMinimumSize(QtCore.QSize(0, 35))
        self.proxy.setObjectName("proxy")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.proxy)
        self.horizontalLayout_5.addLayout(self.formLayout_10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listen_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.listen_btn.setEnabled(False)
        self.listen_btn.setObjectName("listen_btn")
        self.verticalLayout_3.addWidget(self.listen_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.source_language = QtWidgets.QComboBox(self.layoutWidget)
        self.source_language.setMinimumSize(QtCore.QSize(0, 35))
        self.source_language.setObjectName("source_language")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_language)
        self.horizontalLayout.addLayout(self.formLayout_4)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setObjectName("label_3")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.target_language = QtWidgets.QComboBox(self.layoutWidget)
        self.target_language.setMinimumSize(QtCore.QSize(0, 35))
        self.target_language.setObjectName("target_language")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_language)
        self.horizontalLayout.addLayout(self.formLayout_5)
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_11.setObjectName("formLayout_11")
        self.tts_text = QtWidgets.QLabel(self.layoutWidget)
        self.tts_text.setMinimumSize(QtCore.QSize(0, 35))
        self.tts_text.setObjectName("tts_text")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tts_text)
        self.tts_type = QtWidgets.QComboBox(self.layoutWidget)
        self.tts_type.setMinimumSize(QtCore.QSize(0, 35))
        self.tts_type.setObjectName("tts_type")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tts_type)
        self.horizontalLayout.addLayout(self.formLayout_11)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 35))
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.voice_role = QtWidgets.QComboBox(self.layoutWidget)
        self.voice_role.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_role.setObjectName("voice_role")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_role)
        self.horizontalLayout.addLayout(self.formLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 35))
        self.label_5.setObjectName("label_5")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.whisper_model = QtWidgets.QComboBox(self.layoutWidget)
        self.whisper_model.setMinimumSize(QtCore.QSize(0, 35))
        self.whisper_model.setObjectName("whisper_model")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.whisper_model)
        self.horizontalLayout_2.addLayout(self.formLayout_7)
        self.formLayout_13 = QtWidgets.QFormLayout()
        self.formLayout_13.setObjectName("formLayout_13")
        self.whisper_type = QtWidgets.QComboBox(self.layoutWidget)
        self.whisper_type.setMinimumSize(QtCore.QSize(0, 35))
        self.whisper_type.setObjectName("whisper_type")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.whisper_type)
        self.horizontalLayout_2.addLayout(self.formLayout_13)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 35))
        self.label_6.setObjectName("label_6")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.voice_rate = QtWidgets.QLineEdit(self.layoutWidget)
        self.voice_rate.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_rate.setObjectName("voice_rate")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_rate)
        self.horizontalLayout_2.addLayout(self.formLayout_8)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 35))
        self.label_7.setObjectName("label_7")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.voice_silence = QtWidgets.QLineEdit(self.layoutWidget)
        self.voice_silence.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_silence.setObjectName("voice_silence")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_silence)
        self.horizontalLayout_2.addLayout(self.formLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 35))
        self.label_8.setObjectName("label_8")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.subtitle_type = QtWidgets.QComboBox(self.layoutWidget)
        self.subtitle_type.setMinimumSize(QtCore.QSize(0, 35))
        self.subtitle_type.setCurrentText("")
        self.subtitle_type.setObjectName("subtitle_type")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subtitle_type)
        self.horizontalLayout_4.addLayout(self.formLayout_12)
        self.voice_autorate = QtWidgets.QCheckBox(self.layoutWidget)
        self.voice_autorate.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_autorate.setObjectName("voice_autorate")
        self.horizontalLayout_4.addWidget(self.voice_autorate)
        self.enable_cuda = QtWidgets.QCheckBox(self.layoutWidget)
        self.enable_cuda.setMinimumSize(QtCore.QSize(0, 35))
        self.enable_cuda.setObjectName("enable_cuda")
        self.horizontalLayout_4.addWidget(self.enable_cuda)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startbtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy)
        self.startbtn.setMinimumSize(QtCore.QSize(200, 50))
        self.startbtn.setObjectName("startbtn")
        self.horizontalLayout_3.addWidget(self.startbtn)
        self.continue_compos = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_compos.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_compos.sizePolicy().hasHeightForWidth())
        self.continue_compos.setSizePolicy(sizePolicy)
        self.continue_compos.setMinimumSize(QtCore.QSize(260, 35))
        self.continue_compos.setText("")
        self.continue_compos.setObjectName("continue_compos")
        self.horizontalLayout_3.addWidget(self.continue_compos)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.process = QtWidgets.QTextBrowser(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process.sizePolicy().hasHeightForWidth())
        self.process.setSizePolicy(sizePolicy)
        self.process.setMinimumSize(QtCore.QSize(0, 100))
        self.process.setAutoFillBackground(False)
        self.process.setStyleSheet("border:0;\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.process.setReadOnly(True)
        self.process.setObjectName("process")
        self.verticalLayout_2.addWidget(self.process)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.subtitle_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.subtitle_layout.setContentsMargins(0, 0, 0, 0)
        self.subtitle_layout.setObjectName("subtitle_layout")
        self.horizontalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_Key = QtWidgets.QMenu(self.menuBar)
        self.menu_Key.setObjectName("menu_Key")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_H = QtWidgets.QMenu(self.menuBar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menuBar)
        self.actionbaidu_key = QtWidgets.QAction(MainWindow)
        self.actionbaidu_key.setObjectName("actionbaidu_key")
        self.actionchatgpt_key = QtWidgets.QAction(MainWindow)
        self.actionchatgpt_key.setObjectName("actionchatgpt_key")
        self.actiondeepL_key = QtWidgets.QAction(MainWindow)
        self.actiondeepL_key.setObjectName("actiondeepL_key")
        self.action_tool = QtWidgets.QAction(MainWindow)
        self.action_tool.setObjectName("action_tool")
        self.action_vlc = QtWidgets.QAction(MainWindow)
        self.action_vlc.setObjectName("action_vlc")
        self.action_ffmpeg = QtWidgets.QAction(MainWindow)
        self.action_ffmpeg.setObjectName("action_ffmpeg")
        self.action_git = QtWidgets.QAction(MainWindow)
        self.action_git.setObjectName("action_git")
        self.action_issue = QtWidgets.QAction(MainWindow)
        self.action_issue.setObjectName("action_issue")
        self.action_clone = QtWidgets.QAction(MainWindow)
        self.action_clone.setObjectName("action_clone")
        self.actiondeepLX_address = QtWidgets.QAction(MainWindow)
        self.actiondeepLX_address.setObjectName("actiondeepLX_address")
        self.menu_Key.addAction(self.actionbaidu_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionchatgpt_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepL_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepLX_address)
        self.menu_Key.addSeparator()
        self.menu.addAction(self.action_tool)
        self.menu.addSeparator()
        self.menu.addAction(self.action_clone)
        self.menu_H.addAction(self.action_git)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_issue)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_vlc)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_ffmpeg)
        self.menuBar.addAction(self.menu_Key.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SP Video Translate & Doubbing"))
        self.btn_get_video.setToolTip(_translate("MainWindow", "可选择多个mp4视频，自动排队处理"))
        self.btn_get_video.setText(_translate("MainWindow", "Video to be"))
        self.source_mp4.setPlaceholderText(_translate("MainWindow", "Select multiple MP4 videos to be translated and queue up for processing"))
        self.btn_save_dir.setText(_translate("MainWindow", "Save to.."))
        self.target_dir.setPlaceholderText(_translate("MainWindow", "Select the location to save the translated video to, which defaults to the original directory_ Video_ Out"))
        self.label_9.setText(_translate("MainWindow", "TranslChannels"))
        self.label.setText(_translate("MainWindow", "NetworkProxy"))
        self.proxy.setPlaceholderText(_translate("MainWindow", "For example http://127.0.0.1:10809 Required in Chinese Mainland"))
        self.listen_btn.setText(_translate("MainWindow", "listen voice"))
        self.label_2.setText(_translate("MainWindow", "SourceLanguage"))
        self.source_language.setToolTip(_translate("MainWindow", "视频原始语音所用语言"))
        self.label_3.setText(_translate("MainWindow", "TargetLanguage"))
        self.target_language.setToolTip(_translate("MainWindow", "你希望翻译为哪种语言"))
        self.tts_text.setText(_translate("MainWindow", "TTS"))
        self.label_4.setText(_translate("MainWindow", "Role"))
        self.voice_role.setToolTip(_translate("MainWindow", "选No代表不进行配音"))
        self.label_5.setText(_translate("MainWindow", "VoiceModels"))
        self.whisper_model.setToolTip(_translate("MainWindow", "base到large，效果越来越好，但速度也越来越慢"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.voice_rate.setToolTip(_translate("MainWindow", "是否加速或减速播放配音"))
        self.voice_rate.setPlaceholderText(_translate("MainWindow", "Positive numbers accelerate, negative numbers decelerate, -90 to+90"))
        self.label_7.setText(_translate("MainWindow", "Silent duration"))
        self.voice_silence.setToolTip(_translate("MainWindow", "默认500ms，越小切分的片段越多"))
        self.voice_silence.setPlaceholderText(_translate("MainWindow", "Mute duration of segmented speech, in ms"))
        self.label_8.setText(_translate("MainWindow", "SubtitleType"))
        self.subtitle_type.setToolTip(_translate("MainWindow", "嵌入式字幕无论哪里播放始终显示字幕，不可隐藏。\n"
"软字幕如果播放器支持，可在播放器中控制显示或隐藏。\n"
"如果你想网页中播放时显示字幕，请选择嵌入式字幕。\n"
""))
        self.voice_autorate.setToolTip(_translate("MainWindow", "如果配音后时长大于原时长，是否强制加速播放"))
        self.voice_autorate.setText(_translate("MainWindow", "Dubbing automatic acceleration"))
        self.enable_cuda.setToolTip(_translate("MainWindow", "必须确定有N卡且正确配置了CUDA环境，否则勿选"))
        self.enable_cuda.setText(_translate("MainWindow", "EnableCUDA"))
        self.startbtn.setText(_translate("MainWindow", "Start"))
        self.menu_Key.setTitle(_translate("MainWindow", "&SetKey"))
        self.menu.setTitle(_translate("MainWindow", "&Tools"))
        self.menu_H.setTitle(_translate("MainWindow", "&Help"))
        self.actionbaidu_key.setText(_translate("MainWindow", "百度Key"))
        self.actionchatgpt_key.setText(_translate("MainWindow", "OpenAI Key"))
        self.actiondeepL_key.setText(_translate("MainWindow", "DeepL Key"))
        self.action_tool.setText(_translate("MainWindow", "Video ToolBoxs"))
        self.action_tool.setToolTip(_translate("MainWindow", "一个简单的视频处理工具箱"))
        self.action_vlc.setText(_translate("MainWindow", "VLC website"))
        self.action_vlc.setToolTip(_translate("MainWindow", "去VLC官网"))
        self.action_ffmpeg.setText(_translate("MainWindow", "FFmpeg website"))
        self.action_ffmpeg.setToolTip(_translate("MainWindow", "去FFmpeg官网"))
        self.action_git.setText(_translate("MainWindow", "Github Repo"))
        self.action_issue.setText(_translate("MainWindow", "Post issue"))
        self.action_clone.setText(_translate("MainWindow", "Voice Clone"))
        self.actiondeepLX_address.setText(_translate("MainWindow", "DeepLX address"))