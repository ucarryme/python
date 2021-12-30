import win32gui
import win32con
import random
from win32gui import *
while True:
    titles = set()
    def foo(hwnd, Nouse):
            titles.add(GetWindowText(hwnd))
    EnumWindows(foo, 0) 
    if "QQ" in titles:
        QQwin = win32gui.FindWindow("TXGuiFoundation", "QQ")
        x = random.randrange(1900)
        y = random.randrange(1200)
        try:
            # win32gui.ShowWindow(QQwin, win32con.SW_HIDE)
            # time.sleep(1)
            # win32gui.ShowWindow(QQwin, win32con.SW_SHOW)
            # time.sleep(1)
            win32gui.SetWindowPos(QQwin, win32con.HWND_TOPMOST, x, y, 300, 700, win32con.SWP_SHOWWINDOW)
        except:
            continue
'''
import win32gui
import win32con
import  random
from win32gui import *
while True:

    titles = set()
    def foo(hwnd, NULL):			#这里由于要接受EnumWindows(foo, 0)的返回值，虽然参数NULL没有使用，但是也不能不写。
        # if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
            # 筛选IsWindow窗口句柄 and IsWindowEnabled启用的窗口 and IsWindowVisible可视窗口
            #这里也可以用，因为打开QQ，必定会弹出窗口 ，就出现在IsWindowVisible可视窗口里面，
            titles.add(GetWindowText(hwnd))
        # GetWindowText编辑框文字获取
        # hWnd: 带文本的窗口或控制的句柄
    EnumWindows(foo, 0)       #EnumWindows 该函数枚举所有屏幕上的顶层窗口，
    						#参数 0 代表的是所有窗口层级
                            # 并将窗口句柄传送给应用程序定义的回调函数foo。
                            #回调函数返回FALSE将停止枚举，
                            # 否则EnumWindows函数继续到所有顶层窗口枚举完为止。
    # lt = [t for t in titles if t]   #把titles 遍历到list里面
    # lt.sort()                     #

    # if "QQ" in lt:                #因为这里只需要进行一个判断 不用再导入lt 再判断
    if "QQ" in titles:
        QQwin = win32gui.FindWindow("TXGuiFoundation", "QQ") #找到QQ 窗口
        x = random.randrange(1900)
        #time.sleep(1)
        y = random.randrange(1200)
        # time.sleep(1)
        try:
        win32gui.SetWindowPos(QQwin, win32con.HWND_TOPMOST, x, y, 400,400, win32con.SWP_SHOWWINDOW) 
         							#HWND_TOPMOST屏幕窗口层级的最上面  #SWP_SHOWWINDOW显示窗口
      	except:
      		continue
      #最后这里进行一个 try - except 的处理 ，为了解决当qq 运行后关闭，导致脚本出错，终止循环
      #当qq关闭，执行到try：下面的语句如果报错， 则执行except下面的语句 

#后面就可以安装pyinstaller  进行py文件打包成exe文件，
#cmd 进行 制作exe ： pyinstaller -F -w (这里将py文件拖到cmd框里就行，注意和前面的w空格)
#  -F -w   是制作的exe 不需要程序框显示，即后台运行
#如果需要 改为 -F 即可
————————————————
版权声明：本文为CSDN博主「微信-支付宝」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43097301/article/details/83243614
'''