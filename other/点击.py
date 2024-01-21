import time

import pyautogui
import time
def click():
    i=0
    while i<100:


        pyautogui.press('A')
        #time.sleep(0.5)
        i+=1
time.sleep(4)
position = pyautogui.Point(x=483, y=444)
pyautogui.click(position)
click()






























