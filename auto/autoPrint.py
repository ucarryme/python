
import time
import pyautogui
import random
import pyperclip
def is_contain_chinese(word:str):
     '''
     判断一个词是否是非英文词,只要包含一个中文，就认为是非英文词汇
     :param word:
     :return:
     '''
     count = 0
     for s in word.encode('utf-8').decode('utf-8'):
         if u'\u4e00' <= s <= u'\u9fff':
             count += 1
             break
     if count > 0:
         return True
     else:
         return False


pathHead = "E:/study/Learning Python/auto/"
filename = "information.txt"
path = pathHead+filename


time.sleep(3)

with open(path,'r',encoding='u8') as info:
    lines = info.readlines()
while True:
    text = random.choice(lines)
    if is_contain_chinese(text):
        print(text)
        pyperclip.copy(text)
        time.sleep(2)
        pyautogui.hotkey('ctrl','v')
    else:
        pyautogui.typewrite(text,interval= 0.15)

    pyautogui.press('enter')
    time.sleep(3)
# tetcontent = "tamen  yifjing  chufale!"
# for _ in range(10):
#     pyautogui.typewrite(tetcontent,interval = 0.15)
#     pyautogui.press("space")
#     pyautogui.press("enter")
#     time.sleep(2)
