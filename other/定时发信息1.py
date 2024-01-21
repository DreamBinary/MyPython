import pyautogui
import pyperclip
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def main():
    pyautogui.PAUSE = 0

    icon_position = pyautogui.Point(x=655, y=1049)  # 任务栏图标位置578,1063
    entry_position = pyautogui.Point(x=1097, y=542)  # 输入框位置1197, 5401097, 542

    pyautogui.moveTo(icon_position, duration=1)  # duration为执行时长
    pyautogui.click(icon_position)
    pyautogui.moveTo(entry_position, duration=0.5)
    pyautogui.click(entry_position)
    pyperclip.copy('现在是北京时间9：17，竟然还有人在睡觉')#信息
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    '''pyperclip.copy('-----------')#信息
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')'''

scheduler = BlockingScheduler()  # 实例化
scheduler.add_job(main, 'date', run_date=datetime(2021, 10, 2, 9, 17, 00))  # 添加任务
scheduler.start()
























