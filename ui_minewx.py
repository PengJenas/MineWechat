# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_minewx.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 600)
        Form.setMinimumSize(QtCore.QSize(850, 600))
        Form.setMaximumSize(QtCore.QSize(850, 600))
        self.verticalWidget_1 = QtWidgets.QWidget(Form)
        self.verticalWidget_1.setGeometry(QtCore.QRect(0, 0, 60, 600))
        self.verticalWidget_1.setMinimumSize(QtCore.QSize(60, 600))
        self.verticalWidget_1.setMaximumSize(QtCore.QSize(60, 600))
        self.verticalWidget_1.setStyleSheet("QWidget#verticalWidget_1{\n"
"background-color: rgb(67, 67, 67);\n"
"}\n"
"QLabel{\n"
"font: 12pt;\n"
"color:#FFFFFF;\n"
"padding:0px 0px 0px 3px;\n"
"}\n"
"QLabel:hover,QLabel:presse{\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"QToolButton{\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"padding:15px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"QToolButton:checked{\n"
"background-color: rgb(180, 180, 180);\n"
"}\n"
"")
        self.verticalWidget_1.setObjectName("verticalWidget_1")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalWidget_1)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.label_name = QtWidgets.QLabel(self.verticalWidget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QtCore.QSize(60, 60))
        self.label_name.setSizeIncrement(QtCore.QSize(40, 40))
        self.label_name.setObjectName("label_name")
        self.verticalLayout_1.addWidget(self.label_name, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.toolButton_11friend = QtWidgets.QToolButton(self.verticalWidget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_11friend.sizePolicy().hasHeightForWidth())
        self.toolButton_11friend.setSizePolicy(sizePolicy)
        self.toolButton_11friend.setMinimumSize(QtCore.QSize(60, 60))
        self.toolButton_11friend.setMaximumSize(QtCore.QSize(60, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/好友列表.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11friend.setIcon(icon)
        self.toolButton_11friend.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_11friend.setCheckable(True)
        self.toolButton_11friend.setObjectName("toolButton_11friend")
        self.buttonGroup_left = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_left.setObjectName("buttonGroup_left")
        self.buttonGroup_left.addButton(self.toolButton_11friend)
        self.verticalLayout_1.addWidget(self.toolButton_11friend)
        self.toolButton_12chatroom = QtWidgets.QToolButton(self.verticalWidget_1)
        self.toolButton_12chatroom.setMinimumSize(QtCore.QSize(60, 60))
        self.toolButton_12chatroom.setMaximumSize(QtCore.QSize(60, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/images/群聊.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12chatroom.setIcon(icon1)
        self.toolButton_12chatroom.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_12chatroom.setCheckable(True)
        self.toolButton_12chatroom.setObjectName("toolButton_12chatroom")
        self.buttonGroup_left.addButton(self.toolButton_12chatroom)
        self.verticalLayout_1.addWidget(self.toolButton_12chatroom)
        self.toolButton_13more = QtWidgets.QToolButton(self.verticalWidget_1)
        self.toolButton_13more.setMinimumSize(QtCore.QSize(60, 60))
        self.toolButton_13more.setMaximumSize(QtCore.QSize(60, 60))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/功能管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13more.setIcon(icon2)
        self.toolButton_13more.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_13more.setCheckable(True)
        self.toolButton_13more.setObjectName("toolButton_13more")
        self.buttonGroup_left.addButton(self.toolButton_13more)
        self.verticalLayout_1.addWidget(self.toolButton_13more)
        spacerItem = QtWidgets.QSpacerItem(60, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_1.addItem(spacerItem)
        self.toolButton_18login = QtWidgets.QToolButton(self.verticalWidget_1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/images/扫码.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_18login.setIcon(icon3)
        self.toolButton_18login.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_18login.setObjectName("toolButton_18login")
        self.verticalLayout_1.addWidget(self.toolButton_18login)
        self.toolButton_19logout = QtWidgets.QToolButton(self.verticalWidget_1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/images/登出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_19logout.setIcon(icon4)
        self.toolButton_19logout.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_19logout.setObjectName("toolButton_19logout")
        self.verticalLayout_1.addWidget(self.toolButton_19logout)
        self.verticalWidget_2 = QtWidgets.QWidget(Form)
        self.verticalWidget_2.setGeometry(QtCore.QRect(60, 0, 250, 600))
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(250, 600))
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(250, 600))
        self.verticalWidget_2.setStyleSheet("QWidget{\n"
"background-color: rgb(230, 230, 230);\n"
"}\n"
"QLineEdit{\n"
"font: 12pt;\n"
"border-radius:5px;\n"
"background-color: rgb(216, 216, 216);\n"
"}\n"
"/*QLineEdit::focus{\n"
"border: 0px solid  white;\n"
"}*/\n"
"QToolButton#toolButton_search{\n"
"background-color: rgb(216, 216, 216);\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"padding:2px;\n"
"}\n"
"QToolButton#toolButton_search:hover{\n"
"background-color:rgb(200, 200, 200);\n"
"}\n"
"QListView{\n"
"font: 12pt;\n"
"background-color: rgb(230, 230, 230);\n"
"border-radius:15px;\n"
"border-style:solid;\n"
"border-width:0px;\n"
"margin:15px;\n"
"}\n"
"")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_21 = QtWidgets.QWidget(self.verticalWidget_2)
        self.horizontalLayout_21.setMinimumSize(QtCore.QSize(250, 50))
        self.horizontalLayout_21.setMaximumSize(QtCore.QSize(250, 50))
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayout_21)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search = QtWidgets.QLineEdit(self.horizontalLayout_21)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(190, 28))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(190, 28))
        self.lineEdit_search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.toolButton_search = QtWidgets.QToolButton(self.horizontalLayout_21)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/images/搜索.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_search.setIcon(icon5)
        self.toolButton_search.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_search.setObjectName("toolButton_search")
        self.horizontalLayout_2.addWidget(self.toolButton_search)
        self.verticalLayout_2.addWidget(self.horizontalLayout_21)
        self.verticalWidget_22 = QtWidgets.QWidget(self.verticalWidget_2)
        self.verticalWidget_22.setObjectName("verticalWidget_22")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalWidget_22)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.stackedWidget_1 = QtWidgets.QStackedWidget(self.verticalWidget_22)
        self.stackedWidget_1.setAcceptDrops(False)
        self.stackedWidget_1.setAccessibleName("")
        self.stackedWidget_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget_1.setLineWidth(1)
        self.stackedWidget_1.setObjectName("stackedWidget_1")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setStyleSheet("")
        self.page_21.setObjectName("page_21")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_21)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView_friend = QtWidgets.QListView(self.page_21)
        self.listView_friend.setStyleSheet("")
        self.listView_friend.setObjectName("listView_friend")
        self.verticalLayout.addWidget(self.listView_friend)
        self.stackedWidget_1.addWidget(self.page_21)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setStyleSheet("")
        self.page_22.setObjectName("page_22")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_22)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listView_chatroom = QtWidgets.QListView(self.page_22)
        self.listView_chatroom.setStyleSheet("")
        self.listView_chatroom.setObjectName("listView_chatroom")
        self.verticalLayout_4.addWidget(self.listView_chatroom)
        self.stackedWidget_1.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_23)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalWidget_23 = QtWidgets.QWidget(self.page_23)
        self.verticalWidget_23.setStyleSheet("QToolButton{\n"
"font: 16pt;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"padding:15px 60px;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"QToolButton:checked{\n"
"background-color: rgb(180, 180, 180);\n"
"}")
        self.verticalWidget_23.setObjectName("verticalWidget_23")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.verticalWidget_23)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        spacerItem1 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_23.addItem(spacerItem1)
        self.toolButton_21remote = QtWidgets.QToolButton(self.verticalWidget_23)
        self.toolButton_21remote.setMinimumSize(QtCore.QSize(250, 60))
        self.toolButton_21remote.setMaximumSize(QtCore.QSize(250, 60))
        self.toolButton_21remote.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_21remote.setAutoFillBackground(False)
        self.toolButton_21remote.setInputMethodHints(QtCore.Qt.ImhNone)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/images/远程协助.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21remote.setIcon(icon6)
        self.toolButton_21remote.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_21remote.setCheckable(True)
        self.toolButton_21remote.setChecked(False)
        self.toolButton_21remote.setAutoRepeat(False)
        self.toolButton_21remote.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_21remote.setAutoRaise(False)
        self.toolButton_21remote.setObjectName("toolButton_21remote")
        self.buttonGroup_mid = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_mid.setObjectName("buttonGroup_mid")
        self.buttonGroup_mid.addButton(self.toolButton_21remote)
        self.verticalLayout_23.addWidget(self.toolButton_21remote)
        self.toolButton_22reply = QtWidgets.QToolButton(self.verticalWidget_23)
        self.toolButton_22reply.setMinimumSize(QtCore.QSize(250, 60))
        self.toolButton_22reply.setMaximumSize(QtCore.QSize(250, 60))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/images/回复.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22reply.setIcon(icon7)
        self.toolButton_22reply.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_22reply.setCheckable(True)
        self.toolButton_22reply.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_22reply.setObjectName("toolButton_22reply")
        self.buttonGroup_mid.addButton(self.toolButton_22reply)
        self.verticalLayout_23.addWidget(self.toolButton_22reply)
        self.toolButton_23help = QtWidgets.QToolButton(self.verticalWidget_23)
        self.toolButton_23help.setMinimumSize(QtCore.QSize(250, 60))
        self.toolButton_23help.setMaximumSize(QtCore.QSize(250, 60))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/images/帮助.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_23help.setIcon(icon8)
        self.toolButton_23help.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_23help.setCheckable(True)
        self.toolButton_23help.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_23help.setObjectName("toolButton_23help")
        self.buttonGroup_mid.addButton(self.toolButton_23help)
        self.verticalLayout_23.addWidget(self.toolButton_23help)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.verticalWidget_23)
        self.stackedWidget_1.addWidget(self.page_23)
        self.verticalLayout_22.addWidget(self.stackedWidget_1)
        self.verticalLayout_2.addWidget(self.verticalWidget_22)
        self.verticalWidget_3 = QtWidgets.QWidget(Form)
        self.verticalWidget_3.setGeometry(QtCore.QRect(310, 0, 546, 600))
        self.verticalWidget_3.setMinimumSize(QtCore.QSize(0, 600))
        self.verticalWidget_3.setMaximumSize(QtCore.QSize(16777215, 600))
        self.verticalWidget_3.setStyleSheet("QWidget#verticalWidget_3{\n"
"background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalWidget_31 = QtWidgets.QWidget(self.verticalWidget_3)
        self.horizontalWidget_31.setMinimumSize(QtCore.QSize(540, 20))
        self.horizontalWidget_31.setMaximumSize(QtCore.QSize(540, 20))
        self.horizontalWidget_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalWidget_31.setStyleSheet("QToolButton{\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"padding:0px 8px;\n"
"/*margin:5px;*/\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(200, 200, 200);\n"
"}")
        self.horizontalWidget_31.setObjectName("horizontalWidget_31")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.horizontalWidget_31)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem3)
        self.toolButton_33hide = QtWidgets.QToolButton(self.horizontalWidget_31)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/images/隐藏.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_33hide.setIcon(icon9)
        self.toolButton_33hide.setIconSize(QtCore.QSize(30, 20))
        self.toolButton_33hide.setObjectName("toolButton_33hide")
        self.horizontalLayout_31.addWidget(self.toolButton_33hide)
        self.verticalLayout_3.addWidget(self.horizontalWidget_31)
        self.verticalWidget_32 = QtWidgets.QWidget(self.verticalWidget_3)
        self.verticalWidget_32.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalWidget_32.setMaximumSize(QtCore.QSize(16777215, 540))
        self.verticalWidget_32.setStyleSheet("QLabel{\n"
"font: 16pt ;\n"
"padding:0px 16px 0px 16px;\n"
"border-style:solid;\n"
"border-width:0px 0px 1px 0px;\n"
"border-color: rgb(200, 200, 200);\n"
"}\n"
"QTextEdit{\n"
"color: rgb(50, 50, 50);\n"
"padding:0px 16px 0px 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"}\n"
"QTextEdit#textEdit_friend_record,QTextEdit#textEdit_chatroom_record{\n"
"background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"border-style:solid;\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:0px 0px 0px 0px;\n"
"}\n"
"/* 标签样式 */\n"
"QTabBar:tab {\n"
"    width: 270px;\n"
"    height: 25px;\n"
"    font: 12pt;\n"
"    border-style:solid;\n"
"    border-width:0px 0px 1px 0px;\n"
"    border-bottom-color:rgb(216, 216, 216);\n"
"}\n"
"\n"
"/* 标签被选中时或鼠标悬浮时 */\n"
"QTabBar:tab:selected,QTabBar:tab:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"    border-bottom-color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton{\n"
"margin:2px 40px;\n"
"border-radius: 5px;\n"
"font: 12pt ;\n"
"border-style:solid;\n"
"background-color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"QCheckBox{\n"
"margin: 15px 0px ;\n"
"}")
        self.verticalWidget_32.setObjectName("verticalWidget_32")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.verticalWidget_32)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.verticalWidget_32)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_31 = QtWidgets.QWidget()
        self.page_31.setObjectName("page_31")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_31)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalWidget = QtWidgets.QWidget(self.page_31)
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_text_friend = QtWidgets.QLabel(self.verticalWidget)
        self.label_text_friend.setMinimumSize(QtCore.QSize(0, 35))
        self.label_text_friend.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_text_friend.setObjectName("label_text_friend")
        self.verticalLayout_8.addWidget(self.label_text_friend)
        self.textEdit_friend_record = QtWidgets.QTextEdit(self.verticalWidget)
        self.textEdit_friend_record.setEnabled(True)
        self.textEdit_friend_record.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit_friend_record.setObjectName("textEdit_friend_record")
        self.verticalLayout_8.addWidget(self.textEdit_friend_record)
        self.verticalLayout_5.addWidget(self.verticalWidget)
        self.tabWidget_friend = QtWidgets.QTabWidget(self.page_31)
        self.tabWidget_friend.setMinimumSize(QtCore.QSize(0, 200))
        self.tabWidget_friend.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabWidget_friend.setObjectName("tabWidget_friend")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_text_friend = QtWidgets.QTextEdit(self.tab)
        self.textEdit_text_friend.setGeometry(QtCore.QRect(1, 1, 541, 151))
        self.textEdit_text_friend.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_text_friend.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_text_friend.setObjectName("textEdit_text_friend")
        self.pushButton_text_helper = QtWidgets.QPushButton(self.tab)
        self.pushButton_text_helper.setGeometry(QtCore.QRect(1, 146, 269, 30))
        self.pushButton_text_helper.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_text_helper.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_text_helper.setObjectName("pushButton_text_helper")
        self.pushButton_text_friend = QtWidgets.QPushButton(self.tab)
        self.pushButton_text_friend.setGeometry(QtCore.QRect(270, 146, 269, 30))
        self.pushButton_text_friend.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_text_friend.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_text_friend.setObjectName("pushButton_text_friend")
        self.tabWidget_friend.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_open_file = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_open_file.setGeometry(QtCore.QRect(0, 20, 541, 30))
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.lineEdit_file_dir = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_file_dir.setGeometry(QtCore.QRect(40, 70, 460, 30))
        self.lineEdit_file_dir.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lineEdit_file_dir.setObjectName("lineEdit_file_dir")
        self.pushButton_file_helper = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_file_helper.setGeometry(QtCore.QRect(1, 146, 269, 30))
        self.pushButton_file_helper.setObjectName("pushButton_file_helper")
        self.pushButton_file_friend = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_file_friend.setGeometry(QtCore.QRect(270, 146, 269, 30))
        self.pushButton_file_friend.setObjectName("pushButton_file_friend")
        self.tabWidget_friend.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget_friend)
        self.stackedWidget_2.addWidget(self.page_31)
        self.page_32 = QtWidgets.QWidget()
        self.page_32.setObjectName("page_32")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_32)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalWidget_4 = QtWidgets.QWidget(self.page_32)
        self.verticalWidget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_text_chatroom = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_text_chatroom.setMinimumSize(QtCore.QSize(0, 35))
        self.label_text_chatroom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_text_chatroom.setObjectName("label_text_chatroom")
        self.verticalLayout_10.addWidget(self.label_text_chatroom)
        self.textEdit_chatroom_record = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.textEdit_chatroom_record.setEnabled(True)
        self.textEdit_chatroom_record.setObjectName("textEdit_chatroom_record")
        self.verticalLayout_10.addWidget(self.textEdit_chatroom_record)
        self.verticalLayout_7.addWidget(self.verticalWidget_4)
        self.tabWidget_chatroom = QtWidgets.QTabWidget(self.page_32)
        self.tabWidget_chatroom.setMinimumSize(QtCore.QSize(0, 200))
        self.tabWidget_chatroom.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabWidget_chatroom.setObjectName("tabWidget_chatroom")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_text_chatroom = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_text_chatroom.setGeometry(QtCore.QRect(0, 146, 540, 30))
        self.pushButton_text_chatroom.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_text_chatroom.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_text_chatroom.setObjectName("pushButton_text_chatroom")
        self.textEdit_text_chatroom = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_text_chatroom.setGeometry(QtCore.QRect(1, 1, 541, 151))
        self.textEdit_text_chatroom.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_text_chatroom.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_text_chatroom.setObjectName("textEdit_text_chatroom")
        self.textEdit_text_chatroom.raise_()
        self.pushButton_text_chatroom.raise_()
        self.tabWidget_chatroom.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_open_file_1 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_open_file_1.setGeometry(QtCore.QRect(0, 20, 540, 30))
        self.pushButton_open_file_1.setObjectName("pushButton_open_file_1")
        self.lineEdit_file_dir_1 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_file_dir_1.setGeometry(QtCore.QRect(40, 70, 460, 30))
        self.lineEdit_file_dir_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lineEdit_file_dir_1.setObjectName("lineEdit_file_dir_1")
        self.pushButton_file_chatroom = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_file_chatroom.setGeometry(QtCore.QRect(0, 146, 540, 30))
        self.pushButton_file_chatroom.setObjectName("pushButton_file_chatroom")
        self.tabWidget_chatroom.addTab(self.tab_6, "")
        self.verticalLayout_7.addWidget(self.tabWidget_chatroom)
        self.stackedWidget_2.addWidget(self.page_32)
        self.page_33 = QtWidgets.QWidget()
        self.page_33.setObjectName("page_33")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_33)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalWidget1 = QtWidgets.QWidget(self.page_33)
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_text_friend_2 = QtWidgets.QLabel(self.verticalWidget1)
        self.label_text_friend_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_text_friend_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_text_friend_2.setObjectName("label_text_friend_2")
        self.verticalLayout_9.addWidget(self.label_text_friend_2)
        self.checkBox_remote = QtWidgets.QCheckBox(self.verticalWidget1)
        self.checkBox_remote.setMinimumSize(QtCore.QSize(460, 0))
        self.checkBox_remote.setFocusPolicy(QtCore.Qt.TabFocus)
        self.checkBox_remote.setObjectName("checkBox_remote")
        self.verticalLayout_9.addWidget(self.checkBox_remote, 0, QtCore.Qt.AlignHCenter)
        self.textEdit_remote = QtWidgets.QTextEdit(self.verticalWidget1)
        self.textEdit_remote.setEnabled(True)
        self.textEdit_remote.setObjectName("textEdit_remote")
        self.verticalLayout_9.addWidget(self.textEdit_remote)
        self.verticalLayout_11.addWidget(self.verticalWidget1)
        self.stackedWidget_2.addWidget(self.page_33)
        self.page_34 = QtWidgets.QWidget()
        self.page_34.setObjectName("page_34")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_34)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalWidget_5 = QtWidgets.QWidget(self.page_34)
        self.verticalWidget_5.setStyleSheet("QLabel#label_busy{\n"
"font:13px;\n"
"margin:5px;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"border-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.verticalWidget_5)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.checkBox_busy = QtWidgets.QCheckBox(self.verticalWidget_5)
        self.checkBox_busy.setMinimumSize(QtCore.QSize(460, 0))
        self.checkBox_busy.setFocusPolicy(QtCore.Qt.TabFocus)
        self.checkBox_busy.setObjectName("checkBox_busy")
        self.verticalLayout_12.addWidget(self.checkBox_busy, 0, QtCore.Qt.AlignHCenter)
        self.label_busy = QtWidgets.QLabel(self.verticalWidget_5)
        self.label_busy.setMinimumSize(QtCore.QSize(460, 0))
        self.label_busy.setStyleSheet("")
        self.label_busy.setObjectName("label_busy")
        self.verticalLayout_12.addWidget(self.label_busy, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_busy = QtWidgets.QLineEdit(self.verticalWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_busy.sizePolicy().hasHeightForWidth())
        self.lineEdit_busy.setSizePolicy(sizePolicy)
        self.lineEdit_busy.setMinimumSize(QtCore.QSize(420, 30))
        self.lineEdit_busy.setObjectName("lineEdit_busy")
        self.verticalLayout_12.addWidget(self.lineEdit_busy, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem4)
        self.checkBox_robot = QtWidgets.QCheckBox(self.verticalWidget_5)
        self.checkBox_robot.setMinimumSize(QtCore.QSize(460, 0))
        self.checkBox_robot.setFocusPolicy(QtCore.Qt.TabFocus)
        self.checkBox_robot.setChecked(False)
        self.checkBox_robot.setAutoRepeat(False)
        self.checkBox_robot.setObjectName("checkBox_robot")
        self.verticalLayout_12.addWidget(self.checkBox_robot, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.verticalLayout_16.addWidget(self.verticalWidget_5)
        self.stackedWidget_2.addWidget(self.page_34)
        self.page_35 = QtWidgets.QWidget()
        self.page_35.setObjectName("page_35")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_35)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalWidget_13 = QtWidgets.QWidget(self.page_35)
        self.verticalWidget_13.setObjectName("verticalWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_13)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.textEdit_help = QtWidgets.QTextEdit(self.verticalWidget_13)
        self.textEdit_help.setEnabled(True)
        self.textEdit_help.setObjectName("textEdit_help")
        self.verticalLayout_13.addWidget(self.textEdit_help)
        self.verticalLayout_14.addWidget(self.verticalWidget_13)
        self.stackedWidget_2.addWidget(self.page_35)
        self.verticalLayout_32.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.verticalWidget_32)
        self.verticalWidget_33 = QtWidgets.QWidget(self.verticalWidget_3)
        self.verticalWidget_33.setMinimumSize(QtCore.QSize(0, 55))
        self.verticalWidget_33.setMaximumSize(QtCore.QSize(16777215, 40))
        self.verticalWidget_33.setStyleSheet("QTextEdit{\n"
"padding:5px 10px 0px 10px;\n"
"margin:0px;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 0px;\n"
"background-color: rgb(245, 245, 245);\n"
"/*background-color: rgb(255, 255, 255);*/\n"
"}")
        self.verticalWidget_33.setObjectName("verticalWidget_33")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.verticalWidget_33)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.textEdit_output = QtWidgets.QTextEdit(self.verticalWidget_33)
        self.textEdit_output.setEnabled(True)
        self.textEdit_output.setMinimumSize(QtCore.QSize(0, 55))
        self.textEdit_output.setObjectName("textEdit_output")
        self.verticalLayout_33.addWidget(self.textEdit_output)
        self.verticalLayout_3.addWidget(self.verticalWidget_33)

        self.retranslateUi(Form)
        self.stackedWidget_1.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget_friend.setCurrentIndex(0)
        self.tabWidget_chatroom.setCurrentIndex(0)
        self.toolButton_33hide.clicked.connect(Form.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Jenas"))
        self.toolButton_11friend.setText(_translate("Form", "..."))
        self.toolButton_12chatroom.setText(_translate("Form", "..."))
        self.toolButton_13more.setText(_translate("Form", "..."))
        self.toolButton_18login.setText(_translate("Form", "..."))
        self.toolButton_19logout.setText(_translate("Form", "..."))
        self.toolButton_search.setText(_translate("Form", "..."))
        self.toolButton_21remote.setText(_translate("Form", " 远程控制"))
        self.toolButton_22reply.setText(_translate("Form", " 自动回复"))
        self.toolButton_23help.setText(_translate("Form", " 帮助信息"))
        self.toolButton_33hide.setText(_translate("Form", "..."))
        self.label_text_friend.setText(_translate("Form", "好友昵称"))
        self.textEdit_text_friend.setPlaceholderText(_translate("Form", "输入消息..."))
        self.pushButton_text_helper.setText(_translate("Form", "发送至助手"))
        self.pushButton_text_friend.setText(_translate("Form", "发送至好友"))
        self.tabWidget_friend.setTabText(self.tabWidget_friend.indexOf(self.tab), _translate("Form", "文字"))
        self.pushButton_open_file.setText(_translate("Form", "选取文件（暂不支持中文文件名）"))
        self.pushButton_file_helper.setText(_translate("Form", "发送至助手"))
        self.pushButton_file_friend.setText(_translate("Form", "发送至好友"))
        self.tabWidget_friend.setTabText(self.tabWidget_friend.indexOf(self.tab_2), _translate("Form", "文件"))
        self.label_text_chatroom.setText(_translate("Form", "群聊名称"))
        self.pushButton_text_chatroom.setText(_translate("Form", "发送"))
        self.textEdit_text_chatroom.setPlaceholderText(_translate("Form", "输入消息..."))
        self.tabWidget_chatroom.setTabText(self.tabWidget_chatroom.indexOf(self.tab_5), _translate("Form", "文字"))
        self.pushButton_open_file_1.setText(_translate("Form", "选取文件（暂不支持中文文件名）"))
        self.pushButton_file_chatroom.setText(_translate("Form", "发送"))
        self.tabWidget_chatroom.setTabText(self.tabWidget_chatroom.indexOf(self.tab_6), _translate("Form", "文件"))
        self.label_text_friend_2.setText(_translate("Form", "远程控制"))
        self.checkBox_remote.setText(_translate("Form", "手机端微信控制此电脑"))
        self.label.setText(_translate("Form", "自动回复"))
        self.checkBox_busy.setText(_translate("Form", "忙碌回复"))
        self.label_busy.setText(_translate("Form", "编辑回复内容："))
        self.checkBox_robot.setText(_translate("Form", "机器人回复"))
        self.label_2.setText(_translate("Form", "帮助信息"))


import img_rc
