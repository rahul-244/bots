from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con

# X:  288 Y:  340 RGB: (  0,   0,   0)
# X:  366 Y:  340 RGB: (  0,   0,   0)
# X:  455 Y:  340 RGB: (  0,   0,   0)
# X:  521 Y:  340 RGB: (  0,   0,   0)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # Increase to 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if p.pixel(288, 340)[0] == 0:
        click(288, 340)
    if p.pixel(366, 340)[0] == 0:
        click(366, 340)
    if p.pixel(455, 340)[0] == 0:
        click(455, 340)
    if p.pixel(521, 340)[0] == 0:
        click(521, 340)

# https://lagged.com/en/g/magic-tiles