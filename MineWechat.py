# -*- coding: utf-8 -*-
# Author: Jenas

import os
import time
import win32api    # 系统api
import win32con    # 操作键盘
from PIL import ImageGrab    # 截图用
import imghdr    # 识别图像格式
import requests,json    # 爬机器人回复
import itchat    # 微信库
from itchat.content import *
from PyQt5 import QtCore, QtGui, QtWidgets    # PYQT5
from MineUI import Ui_Form    # 程序UI
import img_rc    # 程序图标文件


#########################################################################################################
# MyWindow窗口
#########################################################################################################

class MyWindow(QtWidgets.QWidget,Ui_Form):          # 注意Ui_Form要跟UI文件中的匹配
    def __init__(self):                             
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # 初始化标签、文本框提示
        self.output_info("点击“扫码登录”按钮！")
        self.textEdit_text_friend.setText("输入信息：")
        self.textEdit_text_chatroom.setText("可以@群里的某个人")
        self.textEdit_remote.setText("[帮助信息]手机端微信编辑“#帮助”发送至“文件传输助手”")
        self.lineEdit_busy.setText("您好，我现在忙，不方便回复您！有事请留言！[微笑]")
        # 按钮
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_text_helper.clicked.connect(self.text_to_helper)
        self.pushButton_text_friend.clicked.connect(self.text_to_friend)
        self.pushButton_text_chatroom.clicked.connect(self.text_to_chatroom)
        self.pushButton_open_file.clicked.connect(self.open_file)
        self.pushButton_file_helper.clicked.connect(self.file_to_helper)
        self.pushButton_file_friend.clicked.connect(self.file_to_friend)
        self.pushButton_file_chatroom.clicked.connect(self.file_to_chatroom)
        # 登陆微信前,使按钮失效  
        self.pushButton_logout.setEnabled(False)         
        self.pushButton_text_helper.setEnabled(False)
        self.pushButton_text_friend.setEnabled(False)
        self.pushButton_text_chatroom.setEnabled(False)
        self.pushButton_open_file.setEnabled(False)
        self.pushButton_file_helper.setEnabled(False)
        self.pushButton_file_friend.setEnabled(False)
        self.pushButton_file_chatroom.setEnabled(False)
        # 复选框
        self.checkBox_remote.setChecked(True)   # 默认勾选
        self.checkBox_busy.stateChanged.connect(self.check_busy) 
        self.checkBox_bot.stateChanged.connect(self.check_bot)
        self.checkBox_remote.stateChanged.connect(self.check_remote)


############################################################################################
# 底部系统,包含：登陆、注销、系统信息
############################################################################################

    # 获取当前时间戳,并转格式,外面再套上方括号
    # 就像这样：[18/09/17 18:12:38]
    def get_now_time(self):     
        now_time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime(time.time()))
        time_msg = '[%s]' % now_time
        return time_msg

    # 记录底部的系统信息
    def output_info(self,info): 
        time_msg = self.get_now_time()
        self.textEdit_output.append(time_msg+"[系统信息]"+info)

    # 登陆按钮
    def login(self):
        #print("执行：login")
        self.output_info("请扫描二维码...")
        # 按钮启用和失效
        self.pushButton_login.setEnabled(False)
        self.pushButton_logout.setEnabled(True)
        self.pushButton_text_helper.setEnabled(True)
        self.pushButton_text_friend.setEnabled(True)
        self.pushButton_text_chatroom.setEnabled(True)
        self.pushButton_open_file.setEnabled(True)
        self.pushButton_file_helper.setEnabled(True)
        self.pushButton_file_friend.setEnabled(True)
        self.pushButton_file_chatroom.setEnabled(True)

        # 创建线程
        self.thread = MyThread()
        # 线程的信号槽，依次输出：微信聊天记录、系统登录信息、微信远控信息
        self.thread._signal_1.connect(self.write_log)   
        self.thread._signal_2.connect(self.output_info)
        self.thread._signal_3.connect(self.output_remote_info)
        # 开始线程
        self.thread.start()

    # 注销按钮
    def logout(self):
        # 按钮启用和失效
        self.pushButton_login.setEnabled(True)
        self.pushButton_logout.setEnabled(False)       
        self.pushButton_text_helper.setEnabled(False)
        self.pushButton_text_friend.setEnabled(False)
        self.pushButton_text_chatroom.setEnabled(False)
        self.pushButton_open_file.setEnabled(False)
        self.pushButton_file_helper.setEnabled(False)
        self.pushButton_file_friend.setEnabled(False)
        self.pushButton_file_chatroom.setEnabled(False)
        itchat.logout()
        self.output_info("您已注销微信！")

    
#######################################################################################
# 微信发送文字、文件
#######################################################################################
    
    # 记录聊天信息,包含：发送信息、接收信息
    # 参数:是否群聊，消息内容，消息时间, 依次类型: bool,str,int
    def write_log(self,fromChatroom,message,send_time,):
        myTime = time.strftime("%m-%d %H:%M:%S", time.localtime(send_time))  # "%Y/%m/%d %H:%M:%S"
        msg_data = '[' + myTime + ']  ' + message
        if fromChatroom == False :
            self.textEdit_friend_record.append(msg_data)
        else:
            self.textEdit_chatroom_record.append(msg_data)

    # 发送文字到助手
    def text_to_helper(self):
        #print("执行：text_to_helper")
        text_send = self.textEdit_text_friend.toPlainText()
        itchat.send(text_send, toUserName='filehelper')
        self.output_info("成功发送文字至：文件传输助手")
        fromChatroom = False    # 做个记号，不是群聊
        message = "Python → 助手：" + text_send        # 编辑聊天记录内容
        send_time = time.time()     # 获取当前时间
        self.write_log(fromChatroom,message, send_time)     # 写聊天记录

    # 发送文字到好友
    def text_to_friend(self):
        #print("执行：tex_to_friend")
        text_send = self.textEdit_text_friend.toPlainText()
        text_friend = self.lineEdit_text_friend.text()
        search_username = itchat.search_friends(text_friend)
        if search_username:
            text_username = search_username[0]['UserName']      #用户ID，一长串数字，用于发消息
            text_nickname = search_username[0]['NickName']      #用户昵称
            itchat.send(text_send, toUserName=text_username)
            # itchat.send('来自：MineWechat', toUserName=text_username)
            self.output_info("成功发送文字至：%s" % text_nickname)
            fromChatroom = False
            message = "Python → "+ text_nickname + "：" + text_send
            send_time = time.time()
            self.write_log(fromChatroom,message,send_time)
        else:
            self.output_info("好友昵称出错了！")

    # 发送文字到群聊
    def text_to_chatroom(self):
        #print("执行：text_to_chatroom")
        text_send = self.textEdit_text_chatroom.toPlainText()
        text_chatroom = self.lineEdit_text_chatroom.text()
        search_username = itchat.search_chatrooms(text_chatroom)
        if search_username:
            text_username = search_username[0]['UserName']
            itchat.send(text_send, toUserName=text_username)
            self.output_info("成功发送文字至：[%s]" % text_chatroom)
            fromChatroom = True
            message = "Python → " + text_chatroom + "：" + text_send
            send_time = time.time()
            self.write_log(fromChatroom,message, send_time)
        else:
            self.output_info("群聊名称出错了！")

    # 选择要发送的文件
    def open_file(self):
        file_name, filetype = QtWidgets.QFileDialog.getOpenFileName(self,"选取文件","D:/","All Files (*)")
        self.lineEdit_file_dir.setText(file_name)
    
    # 发送文件给谁呢?
    def file_to_who(self,file_username):
        file_send = self.lineEdit_file_dir.text()
        if imghdr.what(file_send):  # 判断文件是否是图片格式
            itchat.send_image(file_send, toUserName=file_username)
        else:
            itchat.send_file(file_send, toUserName=file_username)

    # 发送文件到助手
    def file_to_helper(self):
        self.file_to_who('filehelper')
        self.output_info("成功发送文件至：文件传输助手")

    # 发送文件到好友
    def file_to_friend(self):
        file_friend = self.lineEdit_file_friend.text()
        search_username = itchat.search_friends(file_friend)
        if search_username:
            file_username = search_username[0]['UserName']      #用户ID，一长串数字，用于发消息
            file_nickname = search_username[0]['NickName']      #用户昵称
            self.file_to_who(file_username)
            self.output_info("成功发送文件至：%s" % file_nickname)
        else:
            self.output_info("好友昵称出错了！")

    # 发送文件到群聊
    def file_to_chatroom(self):
        file_chatroom = self.lineEdit_file_chatroom.text()
        search_username = itchat.search_chatrooms(file_chatroom)
        if search_username:
            file_username = search_username[0]['UserName']
            self.file_to_who(file_username)
            self.output_info("成功发送文件至：群聊[%s]" % file_chatroom)
        else:
            self.output_info("群聊名称出错了！")


###############################################################################
# 功能选项,及远控信息
###############################################################################

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
    def check_bot(self):
        check_state = self.checkBox_bot.checkState()
        #print(check_state)
        global reply_bot
        if check_state == QtCore.Qt.Checked:
            self.output_info('已打开[机器人回复]功能')
            reply_bot =True
        elif check_state == QtCore.Qt.Unchecked:
            self.output_info('已关闭[机器人回复]功能')
            reply_bot = False

    # 调用图灵机器人的api，利用爬虫，根据聊天消息返回回复内容
    def tuling(self,info):
        appkey = "9489eda6f3704a65b0221a3f65e0b98b"
        url = "http://www.tuling123.com/openapi/api?key=%s&info=%s" % (appkey, info)
        req = requests.get(url)
        content = req.text
        data = json.loads(content)
        answer = data['text']
        return answer

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
        remote_info = time_msg + ' ' + message
        self.textEdit_remote.append(remote_info)




#########################################################################################################
# 线程
#########################################################################################################

class MyThread(QtCore.QThread):
    # 定义信号，用于记录聊天信息，含：是否群聊，消息内容，消息时间
    _signal_1 = QtCore.pyqtSignal(bool,str,int)
    # 定义信号，仅用于记录登陆成功的两条系统信息
    _signal_2 = QtCore.pyqtSignal(str)
    # 定义信号,用于记录远控信息
    _signal_3 = QtCore.pyqtSignal(str)
    def __int__(self, parent=None):
        super(MyThread, self).__init__()

    def run(self):
        itchat.auto_login()
        userInfo = itchat.web_init()
        self._signal_2.emit('成功登陆! 账号： %s' % userInfo['User']['NickName'])
        self._signal_2.emit('准备就绪，可以关闭二维码了！')
        itchat.run()




#########################################################################################################
# 处理微信信息
#########################################################################################################

# 私聊信息，文字
@itchat.msg_register(TEXT)
def get_msg(msg):
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    fromChatroom = False
    if msg['FromUserName'] == myUserName:
        # 这是我发出的消息
        from_Name = '我'
        if msg['ToUserName'] == 'filehelper':
            to_Name = '助手'
            if '#' in msg['Text'] and remote_pc == True:    # 执行命令条件：1发给助手 2命令中带井号 3远控开启
                do_what = msg['Text'].split('#')[1]  # #分割，取第二个元素，即：具体指令。
                wechat_do(do_what)
        else:
            to_Name = msg['User'].get('NickName')
    elif msg['ToUserName'] == myUserName:
        # 这是别人发给我的
        if reply_busy == True:  # 自动回复
            msg_busy = myshow.lineEdit_busy.text()
            itchat.send('[自动回复] %s' % msg_busy, msg['FromUserName'])
        if reply_bot == True:   # 机器人回复
            itchat.send('[机器人回复] %s' % myshow.tuling(msg['Text']), msg['FromUserName'])
        to_Name = '我'
        if msg['FromUserName'] == 'filehelper':
            from_Name = '助手'
        else:
            from_Name = msg['User'].get('NickName')
    message = from_Name + ' → ' + to_Name + '：' + str(msg['Text'])
    send_time = msg['CreateTime']
    myshow.thread._signal_1.emit(fromChatroom,message, send_time)       # 信号焕发，连接 write_log


# 私聊信息，图片、视频等
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    fromChatroom = False
    if msg['FromUserName'] == myUserName:
        # 这是我发出的消息
        from_Name = '我'
        if msg['ToUserName'] == 'filehelper':
            to_Name = '助手'
            msg.download(msg.fileName)  # 下载文件
        else:
            to_Name = msg['User'].get('NickName')
    elif msg['ToUserName'] == myUserName:
        # 这是别人发给我的
        msg.download(msg.fileName)      # 下载文件
        if reply_busy == True:
            msg_busy = myshow.lineEdit_busy.text()
            itchat.send('[自动回复] %s' % msg_busy, msg['FromUserName'])
        if reply_bot == True:
            itchat.send('[机器人回复] %s' % myshow.tuling(msg['Text']), msg['FromUserName'])
        to_Name = '我'
        if msg['FromUserName'] == 'filehelper':
            from_Name = '助手'
        else:
            from_Name = msg['User'].get('NickName')
    message =  from_Name + ' → ' + to_Name + '：'+ '[文件：%s]'%msg['FileName']
    send_time = msg['CreateTime']
    myshow.thread._signal_1.emit(fromChatroom, message, send_time)      # 信号焕发，连接 write_log

# 群聊信息,@我的文字信息
@itchat.msg_register(TEXT, isGroupChat=True)
def get_msg_at(msg):
    if msg['isAt']:
        if reply_busy == True:
            msg_busy = myshow.lineEdit_busy.text()
            itchat.send(u'@%s\u2005[自动回复] %s' % (msg['ActualNickName'], msg_busy), msg['FromUserName'])
        if reply_bot == True:
            itchat.send(u'@%s\u2005[机器人回复] %s' % (msg['ActualNickName'],myshow.tuling(msg['Text'])), msg['FromUserName'])
        from_Name = msg['ActualNickName']
        fromChatroom = True
        message = from_Name + ' @ 我' + '：' + str(msg['Text'])
        send_time = msg['CreateTime']
        myshow.thread._signal_1.emit(fromChatroom,message, send_time)       # 信号焕发，连接 write_log




#########################################################################################################
# 微信远程控制
#########################################################################################################

def get_now_time(self):     
    now_time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime(time.time()))
    time_msg = '[%s]' % now_time
    return time_msg


def wechat_do(do_what):
    '''判断并执行具体指令，格式为：命令@参数'''
    myshow.thread._signal_3.emit('[接收指令] ' + do_what)
    if '@' not in do_what:  # 不带参数的指令
        if do_what == '帮助':
            read_me()
        elif do_what == '截图':
            img_to_myself()
        elif do_what == '关机':
            shutdown_pc()
        elif do_what == '取消关机':
            cancel_shutdown()
        elif do_what == '关闭网页':
            close_browser()
        elif do_what == '最小化窗口':
            send_win_d()
        elif do_what == '切换窗口':
            send_alt_tab()
    elif '@' in do_what:  # 带参数的指令
        do_cmd = do_what.split('@')[1]  # @分割，取第二个元素，即：指令的参数
        if '打开@' in do_what:
            run_file(do_cmd)  # 打开文件或程序
        elif '关闭@' in do_what:
            shutdown_process(do_cmd)  # 关闭进程
        elif '网页@' in do_what:
            open_web(do_cmd)  # 打开网页
        elif '控制@' in do_what:
            more_cmd(do_cmd)  # 执行更多cmd命令


def read_me():
    '''帮助信息'''
    readme_msg = '[帮助信息] 指令示例：\n'
    readme_msg += '#帮助\n'
    readme_msg += '#截图\n'
    readme_msg += '#关机\n'
    readme_msg += '#取消关机\n'
    readme_msg += '#打开@d:\\abc.txt\n'
    readme_msg += '#关闭@notepad\n'
    readme_msg += '#网页@www.baidu.com\n'
    readme_msg += '#关闭网页\n'
    readme_msg += r'#控制@explorer c:\windows'+'\n'
    readme_msg += '#最小化窗口\n'
    readme_msg += '#切换窗口\n'
    itchat.send(readme_msg, toUserName='filehelper')        # 发送帮助信息
    myshow.thread._signal_3.emit('[远控信息] 已发送帮助信息')

def img_to_myself():
    '''本机截图'''
    ImageGrab.grab().save('sc_img.png')  # 截图并保存
    itchat.send_image('sc_img.png', toUserName='filehelper')  # 微信发送截图给自己
    send_msg = myshow.get_now_time()  # 执行函数，时间信息
    itchat.send(send_msg, toUserName='filehelper')  # 发送消息，截图时间
    myshow.thread._signal_3.emit('[远控信息] 已发送截图')

def shutdown_pc():
    '''本机关机'''
    os.system('shutdown -s -t 60')  # 执行计算机系统指令，这里是60秒后关机
    send_msg = '[远控信息] 60秒后电脑关机\n取消关机命令:\n#取消关机'  # 发送警告消息，提醒取消指令
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit('[远控信息] 警告：60秒后关机')

def cancel_shutdown():
    '''取消关机'''
    os.system('shutdown -a')
    send_msg = '[远控信息] 此次关机已取消'
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def run_file(do_cmd):
    '''打开文件或程序，文件位置套上英文双引号'''
    # file_cmd = '"' +do_cmd+ '"'
    file_cmd = 'start ' + do_cmd
    os.system(file_cmd)
    send_msg = '[远控信息] 已打开文件/程序：' + do_cmd
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def shutdown_process(do_cmd):
    '''关闭程序'''
    process_cmd = 'taskkill /f /t /im ' + do_cmd + '.exe'
    os.system(process_cmd)
    send_msg = '[远控信息] 已关闭进程：' + do_cmd
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def open_web(do_cmd):
    '''浏览器打开网页'''
    # web_cmd = 'start https://' + do_cmd         # 可以使用默认浏览器打开网页，但接下来关闭浏览器进程时，需要作相应修改
    web_cmd = 'start iexplore https://' + do_cmd  # 使用IE打开网页
    os.system(web_cmd)
    send_msg = '[远控信息] 已打开网页：' + do_cmd
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def close_browser():
    '''关闭IE浏览器，其他浏览器请自行加入进程名'''
    # close_ie = 'tskill iexplore' # 需要设置环境变量
    close_ie = 'taskkill /f /t /im iexplore.exe'
    os.system(close_ie)
    send_msg = '[远控信息] 已关闭IE浏览器'
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def more_cmd(do_cmd):
    '''更多指令，即cmd命令，如：explorer是资源管理器，具体请百度cmd命令大全'''
    os.system(do_cmd)
    send_msg = '[远控信息] 已执行CMD指令：' + do_cmd
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit(send_msg)

def send_2key(key_1, key_2):
    '''发送键盘组合键,key_1,key_2,按键码表'''
    win32api.keybd_event(key_1, 0, 0, 0)  # 键盘按下
    time.sleep(1)
    win32api.keybd_event(key_2, 0, 0, 0)  # 键盘按下
    time.sleep(1)
    win32api.keybd_event(key_2, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
    win32api.keybd_event(key_1, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
    # 不发送信息

def send_win_d():
    '''发送组合键win+D，显示桌面，再按一次显示原程序窗口'''
    send_2key(91, 68)  # 查按键码表 win->91  d->68
    send_msg = '[远控信息] Win+D窗口最小化\n再次发送，还原窗口'
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit('[远控信息] Win+D窗口最小化')

def send_alt_tab():
    '''发送组合键alt+tab，切换窗口'''
    send_2key(18, 9)  # 查按键码表 win->91  d->68
    time.sleep(1)  # 等1秒再执行下面的截图
    img_to_myself()  # 发送截图
    send_msg = '[远控信息] 已切换程序窗口\n当前窗口见上图'
    itchat.send(send_msg, toUserName='filehelper')
    myshow.thread._signal_3.emit('[远控信息] 已切换程序窗口')



#########################################################################################################
# 程序窗口,以及系统托盘
#########################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False) # 关闭窗口,也不关闭应用程序
    myshow = MyWindow()
    myshow.show()
    # 自动回复等功能选项默认开关
    reply_busy = False
    reply_bot = False
    remote_pc = True


    # 在系统托盘处显示图标
    tp = QtWidgets.QSystemTrayIcon(myshow)
    tp.setIcon(QtGui.QIcon(":img/MineWechat.ico"))
    # 设置系统托盘图标的菜单
    a1 = QtWidgets.QAction('&显示(Show)',triggered = myshow.show)   
    def quitApp():
        # 关闭窗体程序
        QtCore.QCoreApplication.instance().quit()
        # 隐藏托盘,防止退出后图标残留
        tp.setVisible(False)    
    a2 = QtWidgets.QAction('&退出(Exit)',triggered = quitApp) # 直接退出可以用QtWidgets.qApp.quit ,但会残留图标直到鼠标经过    
    tpMenu = QtWidgets.QMenu()
    tpMenu.addAction(a1)
    tpMenu.addAction(a2)
    tp.setContextMenu(tpMenu)
    # 不调用show不会显示系统托盘
    tp.show()
    # 托盘信息提示,参数1：标题,参数2：内容,参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
    tp.showMessage('MineWechat','关闭程序窗口, 我依然在这里!',icon=0)
    # 鼠标点击托盘图标
    def act(reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            myshow.show()
    tp.activated.connect(act)
    sys.exit(app.exec_())
