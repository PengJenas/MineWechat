# -*- coding: utf-8 -*-
# Author: Jenas
# Date: 2019-07-31


import os
import sys
import time
import win32api    # pywin32 系统api,linux不兼容
import win32con    # pywin32 操作键盘,linux不兼容
from pypinyin import lazy_pinyin  # 好友列表按拼音排序
import imghdr    # 识别图像格式
from wxpy import Bot,Tuling,embed,Group,User
from wxpy import  TEXT, ATTACHMENT, PICTURE, RECORDING, VIDEO    #, CARD, FRIENDS, MAP, SHARING # 各种消息类型
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_minewx import Ui_Form    # 程序UI文件


#########################################################################################################
# MyWindow窗口
#########################################################################################################

class MyWindow(QtWidgets.QWidget,Ui_Form):          # 注意Ui_Form要跟UI文件中的匹配
    def __init__(self):                             
        super(MyWindow, self).__init__()
        self.setupUi(self)
        #QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))   # 风格
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)		# 右上角只有关闭按钮
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 没有标题栏
        self.setWindowOpacity(0.95) # 透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 初始化标签、文本框提示,禁用不需要输入的文本框
        self.output_info("请点击左侧的扫码按钮！")
        self.lineEdit_busy.setText("您好，我现在忙，不方便回复您！有事请留言！[微笑]")
        self.lineEdit_file_dir.setEnabled(False)
        self.lineEdit_file_dir_1.setEnabled(False)
        
        # 点击左侧按钮联动stackedWidget对应页面
        self.toolButton_11friend.clicked.connect(lambda: self.stackedWidget_1.setCurrentIndex(0))
        self.toolButton_11friend.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.toolButton_12chatroom.clicked.connect(lambda: self.stackedWidget_1.setCurrentIndex(1))
        self.toolButton_12chatroom.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
        self.toolButton_13more.clicked.connect(lambda: self.stackedWidget_1.setCurrentIndex(2))
        def btn_more_clicked():   # 更多功能中，还对应三个按钮
            if self.toolButton_21remote.isChecked():
                self.stackedWidget_2.setCurrentIndex(2)
            elif self.toolButton_22reply.isChecked():
                self.stackedWidget_2.setCurrentIndex(3)
            elif self.toolButton_23help.isChecked():
                self.stackedWidget_2.setCurrentIndex(4)
            else:
                self.stackedWidget_2.setCurrentIndex(2)
        self.toolButton_13more.clicked.connect(btn_more_clicked)
        self.toolButton_21remote.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(2))
        self.toolButton_22reply.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(3))
        self.toolButton_23help.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(4))

        # 按钮
        self.toolButton_18login.clicked.connect(self.login)
        self.toolButton_19logout.clicked.connect(self.logout)
        self.toolButton_search.clicked.connect(lambda: self.lineEdit_search.setText("该功能尚未启用！"))
        self.pushButton_text_helper.clicked.connect(self.text_to_helper)
        self.pushButton_text_friend.clicked.connect(self.text_to_friend)
        self.pushButton_text_chatroom.clicked.connect(self.text_to_chatroom)
        self.pushButton_open_file.clicked.connect(self.open_file)
        self.pushButton_open_file_1.clicked.connect(self.open_file)
        self.pushButton_file_helper.clicked.connect(self.file_to_helper)
        self.pushButton_file_friend.clicked.connect(self.file_to_friend)
        self.pushButton_file_chatroom.clicked.connect(self.file_to_chatroom)
        # 复选框
        self.checkBox_remote.setChecked(True)   # 默认勾选
        self.checkBox_busy.stateChanged.connect(self.check_busy) 
        self.checkBox_robot.stateChanged.connect(self.check_robot)
        self.checkBox_remote.stateChanged.connect(self.check_remote)

        # 登陆微信前,使按钮失效
        #self.toolButton_19logout.setEnabled(False)
        self.pushButton_text_helper.setEnabled(False)
        self.pushButton_text_friend.setEnabled(False)
        self.pushButton_text_chatroom.setEnabled(False)
        self.pushButton_open_file.setEnabled(False)
        self.pushButton_open_file_1.setEnabled(False)
        self.pushButton_file_helper.setEnabled(False)
        self.pushButton_file_friend.setEnabled(False)
        self.pushButton_file_chatroom.setEnabled(False)

        # 提示信息
        text_help = '\n' \
                    '========== ★ 感谢使用 MineWechat V4.1 ★ ==========  By Jenas\n\n' \
                    '1. 作者只是初学者，程序尚有很多Bug，请多包涵，欢迎反馈！\n\n' \
                    '2. 好友、群聊列表支持 Ctrl、Shift 多选，双击清空选择。\n\n' \
                    '3. 获取微信远控指令：手机微信编辑“#帮助”发送至“文件传输助手”。\n\n' \
                    '4. 发送文件的文件名不可以是中文，但路径可以包含中文。\n\n' \
                    '5. 隐藏窗口后，可以在系统托盘中打开程序界面。\n\n' \
                    '6. 锁定屏幕会导致部分功能失效，所以，挂机的话请关闭睡眠和锁屏。\n\n' \
                    '7. 想起来再补……'
        self.textEdit_help.setText(text_help)


    # 按住鼠标，拖动窗口
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


    ####################################################
    # 包含：登陆、注销、系统信息、好友列表
    ####################################################

    # 获取当前时间戳,并转格式
    def get_now_time(self):     
        now_time = time.strftime("%m-%d %H:%M:%S")
        time_msg = '[%s]' % now_time
        return time_msg

    # 记录底部的系统信息
    def output_info(self,info): 
        time_msg = self.get_now_time()
        self.textEdit_output.append(time_msg+' '+info)

    # 登陆按钮
    def login(self):
        self.thread = MyThread()    # 创建线程
        # 线程的信号槽，依次关联：写微信聊天记录、获取微信用户名、写微信远控信息、更新好友列表、更新群聊列表、截图
        self.thread._signal_1.connect(self.write_log)
        self.thread._signal_2.connect(self.get_username)
        self.thread._signal_3.connect(self.output_remote_info)
        self.thread._signal_4.connect(self.update_friends)
        self.thread._signal_5.connect(self.update_chatrooms)
        self.thread._signal_6.connect(self.screenshot)
        self.thread.start()    # 开始线程

    # 注销退出按钮
    def logout(self):
        # myshow.thread.bot.logout()
        # time.sleep(0.2)
        quitApp()#底部托盘的方法

    # 微信用户名
    def get_username(self,username):
        self.username = username
        self.label_name.setText(self.username)
        self.output_info('登录成功，%s，欢迎使用！'%self.username)

    # UI按钮启用，更新好友列表时顺带调用
    def ui_enabled(self):
        self.toolButton_18login.setEnabled(False)
        self.toolButton_19logout.setEnabled(True)
        self.pushButton_text_helper.setEnabled(True)
        self.pushButton_text_friend.setEnabled(True)
        self.pushButton_text_chatroom.setEnabled(True)
        self.pushButton_open_file.setEnabled(True)
        self.pushButton_open_file_1.setEnabled(True)
        self.pushButton_file_helper.setEnabled(True)
        self.pushButton_file_friend.setEnabled(True)
        self.pushButton_file_chatroom.setEnabled(True)
      
    # 左侧好友列表
    def update_friends(self,friends_list):
        self.ui_enabled()  # 启用ui按钮
        self.slm_1 = QtCore.QStringListModel()    # 实例化列表模型
        self.qList_1 = friends_list
        self.slm_1.setStringList(self.qList_1)   # 加载数据列表
        self.listView_friend.setModel(self.slm_1)        # 设置列表视图的模型
        self.listView_friend.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)   # 多选列表
        self.listView_friend.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)       # 不能对表格进行修改（双击重命名等）
        self.listView_friend.clicked.connect(self.friends_clicked)
        self.listView_friend.doubleClicked.connect(self.listView_friend.clearSelection)

    # 点击左侧好友列表
    def friends_clicked(self):
        friends_clicked_name = ''
        friends_clicked_list = []
        for i in self.listView_friend.selectedIndexes():
            friend_Name = i.data()
            friends_clicked_name += friend_Name + ' '
            friends_clicked_list.append(friend_Name)
        num =len(friends_clicked_list)
        if num > 1:
            friends_num = friends_clicked_name + '共计['+str(num)+']人'
            self.label_text_friend.setStyleSheet("QLabel#label_text_friend{font: 10pt;}") # 多选好友时，字号变小
        else:
            friends_num = friends_clicked_name
            self.label_text_friend.setStyleSheet("QLabel#label_text_friend{font: 16pt;}")
        self.label_text_friend.setText(friends_num)
        return friends_clicked_list

    # 左侧群聊列表
    def update_chatrooms(self,chatrooms_list):
        self.slm_2 = QtCore.QStringListModel()    # 实例化列表模型
        self.qList_2 = chatrooms_list
        self.slm_2.setStringList(self.qList_2)   # 加载数据列表
        self.listView_chatroom.setModel(self.slm_2)        # 设置列表视图的模型
        self.listView_chatroom.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)     # 多选列表
        self.listView_chatroom.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)    # 禁止对列表修改（双击重命名）
        self.listView_chatroom.clicked.connect(self.chatrooms_clicked)
        self.listView_chatroom.doubleClicked.connect(self.listView_chatroom.clearSelection)

    # 点击左侧群聊列表
    def chatrooms_clicked(self):
        chatrooms_clicked_name = ''
        chatrooms_clicked_list = []
        for i in self.listView_chatroom.selectedIndexes():
            chatroom_Name = i.data()
            chatrooms_clicked_name += chatroom_Name + ' '
            chatrooms_clicked_list.append(chatroom_Name)
        num = len(chatrooms_clicked_list)
        if num > 1:
            chatrooms_num = chatrooms_clicked_name+'共计['+str(num)+']个群'
            self.label_text_chatroom.setStyleSheet("QLabel#label_text_chatroom{font: 10pt;}")
        else:
            chatrooms_num = chatrooms_clicked_name
            self.label_text_chatroom.setStyleSheet("QLabel#label_text_chatroom{font: 16pt;}")
        self.label_text_chatroom.setText(chatrooms_num)
        return chatrooms_clicked_list
    
    # pyqt5截图
    def screenshot(self,img_name):
        # print('截图')
        # 新建screenshot文件夹，并cd进入
        isPathExist = os.path.exists("screenshot")
        if not isPathExist:
            os.makedirs("screenshot")
        os.chdir("screenshot")
        #pyqt5的截图在子进程中会报错，试试用信号通知主线程截图，可行。
        QtWidgets.QApplication.primaryScreen().grabWindow(QtWidgets.QApplication.desktop().winId()).save(img_name)


    #############################################
    # 功能选项,及远控信息
    #############################################

    # 微信忙碌回复功能开关
    def check_busy(self):
        check_state = self.checkBox_busy.checkState()
        #print(check_state)
        global reply_busy
        if check_state == QtCore.Qt.Checked:
            self.output_info('已打开[忙碌回复]功能')
            reply_busy =True
        elif check_state == QtCore.Qt.Unchecked:
            self.output_info('已关闭[忙碌回复]功能')
            reply_busy = False

    # 微信机器人回复功能开关
    def check_robot(self):
        check_state = self.checkBox_robot.checkState()
        #print(check_state)
        global reply_robot
        if check_state == QtCore.Qt.Checked:
            self.output_info('已打开[机器人回复]功能')
            reply_robot =True
        elif check_state == QtCore.Qt.Unchecked:
            self.output_info('已关闭[机器人回复]功能')
            reply_robot = False

    # 调用图灵机器人的api，利用爬虫，根据聊天消息返回回复内容
    tuling = Tuling(api_key='9489eda6f3704a65b0221a3f65e0b98b')  # wxpy整合了图灵机器人

    # 微信远程控制功能开关
    def check_remote(self):
        check_state = self.checkBox_remote.checkState()
        #print(check_state)
        global remote_pc
        if check_state == QtCore.Qt.Checked:
            self.output_info('已打开[微信远控]功能')
            remote_pc = True
        elif check_state == QtCore.Qt.Unchecked:
            self.output_info('已关闭[微信远控]功能')
            remote_pc = False

    # 记录远程控制相关信息
    def output_remote_info(self,message):       
        time_msg = self.get_now_time()
        self.textEdit_remote.append(time_msg+' '+message)


    ######################################
    # 微信发送文字、文件
    ######################################
    
    # 记录聊天信息,包含：发送信息、接收信息
    # 参数:是否群聊，消息内容，消息时间, 依次类型: bool,str,int
    def write_log(self,fromChatroom,message,send_time):
        myTime = time.strftime(r"%m-%d %H:%M:%S", time.localtime(send_time)) 
        msg_data = '['+myTime+'] '+message
        if fromChatroom == False :
            self.textEdit_friend_record.append(msg_data)
        else:
            self.textEdit_chatroom_record.append(msg_data)

    # 发送文字到助手
    def text_to_helper(self):
        text_send = self.textEdit_text_friend.toPlainText()
        self.thread.bot.file_helper.send(text_send)
        fromChatroom = False    # 做个记号，不是群聊
        message = "Python→助手：" + text_send        # 编辑聊天记录内容
        send_time = time.time()     # 获取当前时间
        self.write_log(fromChatroom,message, send_time)     # 写聊天记录

    # 发送文字到好友
    def text_to_friend(self):
        text_send = self.textEdit_text_friend.toPlainText()
        text_friends = self.friends_clicked()
        #print(text_friends)
        if len(text_friends) == 0:  # 没有勾选,列表空           
            self.output_info("您还没有选择好友！")
        else:
            for friend_element in text_friends:
                search_name = self.thread.bot.friends().search(friend_element)[0]
                #print(search_name)
                if search_name:
                    search_name.send(text_send)
                    fromChatroom = False
                    message = "Python→"+ search_name.name + '：' + text_send
                    send_time = time.time()
                    self.write_log(fromChatroom,message,send_time)               
                else:
                    self.output_info("找不到该好友！")

    # 发送文字到群聊
    def text_to_chatroom(self):
        text_send = self.textEdit_text_chatroom.toPlainText()
        text_chatrooms = self.chatrooms_clicked()
        if len(text_chatrooms) == 0:
            self.output_info("您还没有选择群聊！")
        else:
            for chatroom_element in text_chatrooms:
                search_name = self.thread.bot.groups().search(chatroom_element)[0]
                #print(search_name)
                if search_name:
                    search_name.send(text_send)
                    fromChatroom = True
                    message = "Python→" + search_name.name + '：' + text_send
                    send_time = time.time()
                    self.write_log(fromChatroom,message, send_time)
                else:
                    self.output_info("找不到该群聊!")


    # 选择要发送的文件
    def open_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self,"选取文件",".","All Files (*)")[0]
        self.lineEdit_file_dir.setText(file_name)
        self.lineEdit_file_dir_1.setText(file_name)
    
    # 发送文件给谁
    def file_to_who(self,somebody):
        file_send = self.lineEdit_file_dir.text()
        send_OK = False  # 是否发送成功
        try:
            if imghdr.what(file_send):  # 判断文件是否是图片格式
                somebody.send_image(file_send)
            else:
                somebody.send_file(file_send)
            send_OK = True
        except:
            self.output_info("发送文件失败!请检查文件的路径!") #wxpy 发送文件失败，升级itchat就能解决
        return send_OK

    # 发送文件到助手
    def file_to_helper(self):
        file_helper = self.thread.bot.file_helper
        send_OK = self.file_to_who(file_helper)
        if send_OK:
            fromChatroom = False  # 做个记号，不是群聊
            message = "Python→助手：成功发送文件!" # 编辑聊天记录内容
            send_time = time.time()  # 获取当前时间
            self.write_log(fromChatroom, message, send_time)  # 写聊天记录


    # 发送文件到好友
    def file_to_friend(self):
        file_friends = self.friends_clicked()
        if len(file_friends) == 0:
            self.output_send("您还没有选择好友！")
        else:
            for friend in file_friends:
                search_name = self.thread.bot.friends().search(friend)[0]
                #print(search_name)
                if search_name:
                    send_OK = self.file_to_who(search_name)
                    if send_OK:
                        fromChatroom = False  # 做个记号，不是群聊
                        message = "Python→" + search_name.name + '：成功发送文件!'
                        send_time = time.time()  # 获取当前时间
                        self.write_log(fromChatroom, message, send_time)  # 写聊天记录
                else:
                    self.output_send("找不到该好友！")

    # 发送文件到群聊
    def file_to_chatroom(self):
        file_chatrooms = self.chatrooms_clicked()
        if len(file_chatrooms) == 0:
            self.output_send("您还没有选择群聊！")
        else:
            for chatroom in file_chatrooms:
                search_name = self.thread.bot.groups().search(chatroom)[0]
                #print(search_name)
                if search_name:
                    send_OK = self.file_to_who(search_name)
                    if send_OK:
                        fromChatroom = True # 做个记号，不是群聊
                        message = "Python→" + search_name.name + '：成功发送文件!'
                        send_time = time.time()  # 获取当前时间
                        self.write_log(fromChatroom, message, send_time)  # 写聊天记录
                else:
                    self.output_send("找不到该群聊！")



#########################################################################################################
# 微信线程
#########################################################################################################

class MyThread(QtCore.QThread):   
    _signal_1 = QtCore.pyqtSignal(bool,str,int)    # 定义信号，用于记录聊天信息，含：是否群聊，消息内容，消息时间    
    _signal_2 = QtCore.pyqtSignal(str)             # 定义信号，仅用于传出用户名
    _signal_3 = QtCore.pyqtSignal(str)             # 定义信号，用于记录远控信息
    _signal_4 = QtCore.pyqtSignal(list)            # 定义信号，用于记录好友列表
    _signal_5 = QtCore.pyqtSignal(list)            # 定义信号，用于记录群聊列表
    _signal_6 = QtCore.pyqtSignal(str)             # 定义信号，用于截图

    def __int__(self, parent=None):
        super(MyThread, self).__init__()

    def run(self):
        self.bot = Bot(cache_path=True)
        self.myself = self.bot.self
        self._signal_2.emit(self.myself.name)
        self.get_friendslist()
        self.get_chatroomslist()

        ############################
        # 处理接受到的微信消息
        ############################
        # @self.bot.register(msg_types=TEXT,except_self=False)
        # def just_print(msg):
        #     print(msg)

        # 私聊信息，文字
        @self.bot.register(msg_types=TEXT,except_self=False)
        def get_msg(msg):
            fromChatroom = False
            #print(msg)
            if msg.sender.name== self.myself.name:
                # 这是我发出的消息
                from_Name = '我'
                if msg.receiver.name == '文件传输助手':
                    to_Name = '助手'
                    if '#' in msg.text and remote_pc == True:  # 执行命令条件：1发给助手 2命令中带井号 3远控开启
                        do_what = msg.text.split('#')[1]  # 以#分割，取第二个元素，即：具体指令。
                        self.wechat_do(do_what)  # 调用微信远控的方法
                else:
                    to_Name = msg.chat.name
            elif msg.receiver.name == self.myself.name:
                # 这是别人发给我的
                to_Name = '我'
                if msg.sender.name == '文件传输助手':
                    from_Name = '助手'
                else:
                    from_Name = msg.chat.name
                # 自动回复
                if reply_busy == True:  # 忙碌回复
                    msg_busy = myshow.lineEdit_busy.text()
                    msg.reply('[自动回复] %s' % msg_busy)
                if reply_robot == True:  # 机器人回复
                    myshow.tuling.do_reply(msg) # 调用图灵机器人回复
            message = from_Name + '→' + to_Name + '：' + msg.text
            msg_time = msg.create_time
            #print(msg_time,type(msg_time),str(msg_time))  # wxpy的时间格式是datetime
            send_time = time.mktime(msg_time.timetuple()) #datetime转时间戳
            self._signal_1.emit(fromChatroom, message, send_time)  # 信号焕发，连接 write_log


        # 私聊信息，图片、视频等
        @self.bot.register(chats=User, msg_types=[PICTURE, RECORDING, ATTACHMENT, VIDEO])
        def download_files(msg):
            #print(msg)
            fromChatroom = False
            if msg.sender.name == self.myself.name:
                # 这是我发出的消息
                from_Name = '我'
                if msg.receiver.name == '文件传输助手':
                    to_Name = '助手'
                else:
                    to_Name = msg.chat.name
            elif msg.receiver.name == self.myself.name:
                # 这是别人发给我的
                to_Name = '我'
                if msg.sender.name == '文件传输助手':
                    from_Name = '助手'
                else:
                    from_Name = msg.chat.name
                # 自动回复
                if reply_busy == True:
                    msg_busy = myshow.lineEdit_busy.text()
                    msg.reply('[自动回复] %s' % msg_busy)
                if reply_robot == True:  # 机器人回复
                    myshow.tuling.do_reply(msg)
                    # 新建接收文件夹
            downloadDir = '接收文件'
            if not os.path.exists(downloadDir):  # 目录如果不存在
                os.makedirs(downloadDir)
            workPath = os.getcwd()  # 当前程序工作的路径
            downloadPath = os.path.join(workPath, downloadDir)  # 接收文件的路径
            os.chdir(downloadPath)  # 改变当前工作目录
            msg.get_file(msg.file_name)  # 下载文件
            os.chdir(workPath)
            message = from_Name + '→' + to_Name + '：' + '[文件: %s]' % msg.file_name
            msg_time = msg.create_time
            send_time = time.mktime(msg_time.timetuple()) #datetime转时间戳
            self._signal_1.emit(fromChatroom, message, send_time)  # 信号焕发，连接 write_log


        # 群聊信息,@我的文字信息
        @self.bot.register(chats=Group,msg_types=TEXT)
        def get_msg_at(msg):
            #print(msg)
            if msg.is_at:
                #print(msg.member.name)
                if reply_busy == True:
                    msg_busy = myshow.lineEdit_busy.text()
                    msg.reply(u'@%s\u2005[自动回复] %s' % (msg.member.nick_name, msg_busy))
                if reply_robot == True:
                    myshow.tuling.do_reply(msg)
                from_Name = msg.member.name # 成员名
                chatroom_NickName = msg.chat.name #群聊名
                fromChatroom = True
                message = '[' + chatroom_NickName + '] ' + from_Name + ' ：' + msg.text
                msg_time = msg.create_time
                send_time = time.mktime(msg_time.timetuple())
                self._signal_1.emit(fromChatroom, message, send_time)  # 信号焕发，连接 write_log

        self.bot.join() # 堵塞线程，这里不要用embed()，否则pyinstaller打包无窗口会报错



    # 获取好友列表
    def get_friendslist(self):
        friends_info = self.bot.friends(update=False)
        frinends_list = [friend.name for friend in friends_info] # 好友列表 ['张三','Mango','李四']
        frinends_pinyin = [''.join(lazy_pinyin(frinend)) for frinend in frinends_list]  # 根据好友列表生成拼音列表 ['zhangsan','Mango','lisi']
        dict1 = dict(zip(frinends_pinyin,frinends_list))    # 拼音列表和昵称列表并成字典 {'zhangsan':'张三','Mango':'Mango','lisi':'李四'}
        sort1 = sorted(dict1.items(),key=lambda x:x[0].lower())   # 转小写拼音排序 [('lisi','李四'),('Mango','Mango'),('zhangsan','张三')]
        friends_sorted =[i[1] for i in sort1]  # ['李四','Mango','张三']
        self._signal_4.emit(friends_sorted)

    #获取群聊列表
    def get_chatroomslist(self):
        chatrooms_info = self.bot.groups(update=False)
        chatrooms_list = [chatroom.name for chatroom in chatrooms_info]
        self._signal_5.emit(chatrooms_list)



    #######################################
    # 微信远程控制
    #######################################

    def wechat_do(self, do_what):
        '''判断并执行具体指令，格式为：命令@参数'''
        self._signal_3.emit('[接收指令] ' + do_what)
        remote_switch = {
            '帮助':self.read_me,
            '截图':self.img_to_myself,
            '关机':self.shutdown_pc,
            '取消关机':self.cancel_shutdown,
            '关闭网页':self.close_browser,
            '最小化窗口':self.send_win_d,
            '切换窗口':self.send_alt_tab,
            '打开':self.run_file,
            '关闭':self.shutdown_process,
            '网页':self.open_web,
            '控制':self.more_cmd,
            '忙碌回复开':self.reply_busy_on,
            '忙碌回复关':self.reply_busy_off,
            '机器人回复开':self.reply_robot_on,
            '机器人回复关':self.reply_robot_off
        }
        if '@' not in do_what:  # 不带参数的指令
            try:
                remote_switch[do_what]()
            except:
                pass
        elif '@' in do_what:  # 带参数的指令
            do_at_1 = do_what.split('@')[0]  # @分割，取第一个元素，即：指令
            do_at_2 = do_what.split('@')[1]  # 指令的参数
            try:
                remote_switch[do_at_1](do_at_2)
            except:
                pass


    def read_me(self):
        '''帮助信息'''
        readme_msg = '[帮助信息] 指令示例：\n' \
                     '#帮助\n' \
                     '#截图\n' \
                     '#关机\n' \
                     '#取消关机\n' \
                     '#打开@d:\\abc.txt\n' \
                     '#关闭@notepad\n' \
                     '#网页@www.baidu.com\n' \
                     '#关闭网页\n' \
                     '#控制@explorer c:\\windows\n' \
                     '#最小化窗口\n' \
                     '#切换窗口\n' \
                     '#忙碌回复开\n' \
                     '#忙碌回复关\n' \
                     '#机器人回复开\n' \
                     '#机器人回复关\n'
        self.bot.file_helper.send(readme_msg)        # 发送帮助信息
        self._signal_3.emit('[远控信息] 已发送帮助信息')

    def img_to_myself(self):
        '''截图并发送'''
        timeArray = time.localtime(time.time())
        now_time =  time.strftime("%y/%m/%d %H:%M:%S", timeArray)
        time_msg = '时间: [%s]' % now_time
        filename_time = time.strftime("%y%m%d_%H%M%S", timeArray) # 用时间来命名图片,格式中不能有/ : 和空格
        img_name = filename_time + '.png'
        self._signal_6.emit(img_name) # 信号通知主线程截图
        QtCore.QThread.sleep(1)  # 等一下，等主线程截图...
        isImgExist = os.path.exists(img_name)  # 是否存在
        if not isImgExist:
            QtCore.QThread.sleep(1)   # 再等一等......
        self.bot.file_helper.send_image(img_name)  # 微信发送截图给自己
        os.chdir(current_path)
        # print(os.getcwd())
        self.bot.file_helper.send(time_msg)  # 发送消息，截图时间
        self._signal_3.emit('[远控信息] 已发送截图')

    def shutdown_pc(self):
        '''本机关机'''
        os.system('shutdown -s -t 60')  # 执行计算机系统指令，这里是60秒后关机
        send_msg = '[远控信息] 60秒后电脑关机\n取消关机命令:\n#取消关机'  # 发送警告消息，提醒取消指令
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit('[远控信息] 警告：60秒后关机')

    def cancel_shutdown(self):
        '''取消关机'''
        os.system('shutdown -a')
        send_msg = '[远控信息] 此次关机已取消'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def run_file(self, do_at_2):
        '''打开文件或程序，文件位置套上英文双引号'''
        # file_cmd = '"' +do_at_2+ '"'
        file_cmd = 'start ' + do_at_2
        os.system(file_cmd)
        send_msg = '[远控信息] 已打开文件/程序：' + do_at_2
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def shutdown_process(self, do_at_2):
        '''关闭程序'''
        process_cmd = 'taskkill /f /t /im ' + do_at_2 + '.exe'
        os.system(process_cmd)
        send_msg = '[远控信息] 已关闭进程：' + do_at_2
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def open_web(self, do_at_2):
        '''浏览器打开网页'''
        # web_cmd = 'start https://' + do_at_2         # 可以使用默认浏览器打开网页，但接下来关闭浏览器进程时，需要作相应修改
        web_cmd = 'start iexplore https://' + do_at_2  # 使用IE打开网页
        os.system(web_cmd)
        send_msg = '[远控信息] 已打开网页：' + do_at_2
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def close_browser(self):
        '''关闭IE浏览器，其他浏览器请自行加入进程名'''
        # close_ie = 'tskill iexplore' # 需要设置环境变量
        close_ie = 'taskkill /f /t /im iexplore.exe'
        os.system(close_ie)
        send_msg = '[远控信息] 已关闭IE浏览器'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def more_cmd(self, do_at_2):
        '''更多指令，即cmd命令，如：explorer是资源管理器，具体请百度cmd命令大全'''
        os.system(do_at_2)
        send_msg = '[远控信息] 已执行CMD指令：' + do_at_2
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)


    def send_2key(self, key_1, key_2):
        '''发送键盘组合键,key_1,key_2,查按键码表'''
        win32api.keybd_event(key_1, 0, 0, 0)  # 键盘按下
        time.sleep(1)
        win32api.keybd_event(key_2, 0, 0, 0)  # 键盘按下
        time.sleep(1)
        win32api.keybd_event(key_2, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
        win32api.keybd_event(key_1, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
        # 不发送信息

    def send_win_d(self):
        '''发送组合键win+D，显示桌面，再按一次显示原程序窗口'''
        self.send_2key(91, 68)  # 查按键码表 win->91  d->68
        send_msg = '[远控信息] Win+D窗口最小化\n再次发送，还原窗口'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit('[远控信息] Win+D窗口最小化')

    def send_alt_tab(self):
        '''发送组合键alt+tab，切换窗口'''
        self.send_2key(18, 9)  # 查按键码表 win->91  d->68
        time.sleep(1)  # 等1秒再执行下面的截图
        self.img_to_myself()  # 发送截图
        send_msg = '[远控信息] 已切换程序窗口\n当前窗口见上图'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit('[远控信息] 已切换程序窗口')


    def reply_busy_on(self):
        '''打开忙碌回复'''
        myshow.checkBox_busy.setChecked(True)
        send_msg = '[远控信息] 已打开忙碌回复功能'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def reply_busy_off(self):
        '''关闭忙碌回复'''
        myshow.checkBox_busy.setChecked(False)
        send_msg = '[远控信息] 已关闭忙碌回复功能'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def reply_robot_on(self):
        '''打开机器人回复'''
        myshow.checkBox_robot.setChecked(True)
        send_msg = '[远控信息] 已打开机器人回复功能'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)

    def reply_robot_off(self):
        '''关闭机器人回复'''
        myshow.checkBox_robot.setChecked(False)
        send_msg = '[远控信息] 已关闭机器人回复功能'
        self.bot.file_helper.send(send_msg)
        self._signal_3.emit(send_msg)



#########################################################################################################
# 主程序窗口,以及系统托盘
#########################################################################################################

if __name__ == "__main__":
    current_path = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    # QtWidgets.QApplication.setQuitOnLastWindowClosed(False) # 关闭窗口,也不关闭应用程序
    myshow = MyWindow()
    myshow.show()
    # 自动回复等功能选项默认开关
    reply_busy = False
    reply_robot = False
    remote_pc = True

    # 在系统托盘处显示图标
    tp = QtWidgets.QSystemTrayIcon(myshow)
    tp.setIcon(QtGui.QIcon(":/img/images/wechat.png"))
    # 设置系统托盘图标的菜单
    a1 = QtWidgets.QAction('&显示(Show)', triggered=myshow.show)
    def quitApp():  # 退出程序
        QtCore.QCoreApplication.instance().quit()  # 关闭窗体程序
        tp.setVisible(False)  # 隐藏托盘,防止退出后图标残留
    a2 = QtWidgets.QAction('&退出(Exit)', triggered=quitApp)  # 直接退出可以用QtWidgets.qApp.quit ,但会残留图标直到鼠标经过
    tpMenu = QtWidgets.QMenu()
    tpMenu.addAction(a1)
    tpMenu.addAction(a2)
    tp.setContextMenu(tpMenu)
    # 不调用show不会显示系统托盘
    tp.show()
    # 托盘信息提示,参数1：标题,参数2：内容,参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
    # tp.showMessage('MineWechat','关闭程序窗口，我依然在这里！',icon=0)
    # 鼠标点击托盘图标
    def act(reason):
        if reason == 2 or reason == 3:  # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
            # if reason == 2 :
            myshow.show()
    tp.activated.connect(act)

    sys.exit(app.exec_())
