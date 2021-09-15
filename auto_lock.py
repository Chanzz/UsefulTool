from ctypes import *
import pyautogui
from threading import Timer
import time


def close_windows():
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


def main():
    # 退出信号
    exit = False
    # 当前鼠标位置
    current_x, current_y = pyautogui.position()
    # 半小时后执行
    sleep_timer = Timer(1800, close_windows)
    sleep_timer.start()
    while True:
        # 当鼠标移动或定时器已执行退出
        if exit or not sleep_timer.is_alive():
            return
        time.sleep(2)
        x, y = pyautogui.position()
        if abs(current_x - x) > 10 or abs(current_y - y) > 10:
            close_windows()
            exit = True
            sleep_timer.cancel()


if __name__ == '__main__':
    main()
