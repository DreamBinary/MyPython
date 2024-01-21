from pynput import keyboard
from pynput import mouse
from loguru import logger
from threading import Thread


# 键盘监控---------
def on_press(key):
    print(f'{key} :pushed')


def on_release(key):
    # print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
    lsn.join()


# 鼠标监控---------
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('left was pressed!')
    elif button == mouse.Button.right:
        print('right was pressed!')
        return False
    else:
        print('mid was pressed!')


# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# 监控并记录到日志文件---------
# 定义日志文件
logger.add('demo.log')


def on_press(key):
    logger.debug(f'{key} :pushed')


def on_release(key):
    # print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# 定义f1用于线程1
def f1():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
        lsn.join()


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        logger.debug('left was pressed!')
    elif button == mouse.Button.right:
        logger.debug('right was pressed!')
        return False
    else:
        logger.debug('mid was pressed!')


# 定义f2用于线程2
def f2():
    # Collect events until released
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == '__main__':
    # 起两个线程分别监控键盘和鼠标
    t1 = Thread(target=f1)
    t2 = Thread(target=f2)
    t1.start()
    t2.start()

