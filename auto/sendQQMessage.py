import win32gui

import win32con

import win32clipboard as w

import time

def get_text():

    """
    获取剪贴板文本
    """

    w.OpenClipboard()

    d = w.GetClipboardData(win32con.CF_UNICODETEXT)

    w.CloseClipboard()

    return d

def set_text(a_string):

    """设置剪贴板文本"""

    w.OpenClipboard()
    

    w.EmptyClipboard()

    w.SetClipboardData(win32con.CF_UNICODETEXT, a_string)

    w.CloseClipboard()
    time.sleep(3)

def send_qq(to_who, msg):

    """发送qq消息

    to_who：qq消息接收人

    msg：需要发送的消息

    """
    set_text(msg)

    # 将消息写到剪贴板

    qq = win32gui.FindWindow(None, to_who)

    # 投递剪贴板消息到QQ窗体

    win32gui.SendMessage(qq, 258, 22, 2080193)

    win32gui.SendMessage(qq, 770, 0, 0)

    # 模拟按下回车键

    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

to_who = '你' # 需要qq打开，并且和xxx的消息开着
msg = '范德萨'

i = 3 # 执行次数
while i > 0:

    i -= 1

    send_qq(to_who, msg)

    time.sleep(0.1)