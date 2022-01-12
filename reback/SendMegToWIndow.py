import win32gui
import win32con
import win32clipboard as w
import time
lst = ["hello","world","dont","let","me","down"]
#发送的消息

#窗口名字
name = "你"
#将测试消息复制到剪切板中

#获取窗口句柄
handle = win32gui.FindWindow(None, name)
while 1==1:
    msg = lst[int(time.time())%len(lst)]
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    time.sleep(5)

    #填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    #回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    
