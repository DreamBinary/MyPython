import os
import time
import pyautogui
try:
    while True:
        x, y = pyautogui.position()  # 返回鼠标的坐标
        posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        print(posStr)  # 打印坐标
        time.sleep(3)
        os.system('cls')  # 清楚屏幕
except KeyboardInterrupt:
    print('end....')





























