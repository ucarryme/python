import win32gui
import win32con
import win32clipboard as w
import time
#发送的消息
lst = ["这","是","个","测","代码","吗"]
#发送时间间隔
flashTi = int(5)
#窗口名字
name = "你"
#获取窗口句柄
handle = win32gui.FindWindow(None, name)
#循环次数
loopTis = int(50)
i = int(1)
while i<=loopTis:
    msg = lst[int(time.time())%len(lst)]
    i = i +1
    #将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    time.sleep(flashTi)

    #填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    #回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    
