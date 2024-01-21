import time
import pyautogui
import pyperclip
import winsound
#import os
content = """
丑八怪
"""
time.sleep(4)
for line in list(content.split("\n"))*10:
    if line:
        pyautogui.click(x=1186, y=547)  #鼠标点击并定位到聊天窗口
        pyperclip.copy(line)    #复制该行
        #for i in range (0,10):
           # while i<10:
               # pyautogui.hotkey("ctrl","v") #粘贴
               # i+=1
                #break
        pyautogui.hotkey("ctrl", "v")  # 粘贴
        pyautogui.typewrite("\n")   #发送
        # winsound.Beep(440, 1000)
        '''file = r"D:\MUSIC。\黄霄雲-星辰大海.mp3"
        os.system(file)'''
        # break
        time.sleep(60)




























