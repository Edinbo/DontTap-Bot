import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# Definitions
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
while 1==1:
    while keyboard.is_pressed("Q") == True:
        if pyautogui.pixel(1150, 300)[0] == 0:
            click(1150, 300)
        if pyautogui.pixel(1000, 300)[0] == 0:
            click(1000, 300)
        if pyautogui.pixel(850, 300)[0] == 0:
            click(850, 300)
        if pyautogui.pixel(650, 300)[0] == 0:
            click(650, 300)


        if pyautogui.pixel(1150, 450)[0] == 0:
            click(1150, 450)
        if pyautogui.pixel(1000, 450)[0] == 0:
            click(1000, 450)
        if pyautogui.pixel(850, 450)[0] == 0:
            click(850, 450)
        if pyautogui.pixel(650, 450)[0] == 0:
            click(650, 450)

        if pyautogui.pixel(1150, 600)[0] == 0:
            click(1150, 600)
        if pyautogui.pixel(1000, 600)[0] == 0:
            click(1000, 600)
        if pyautogui.pixel(850, 600)[0] == 0:
            click(850, 600)
        if pyautogui.pixel(650, 600)[0] == 0:
            click(650, 600)

        if pyautogui.pixel(1150, 800)[0] == 0:
            click(1150, 800)
        if pyautogui.pixel(1000, 800)[0] == 0:
            click(1000, 800)
        if pyautogui.pixel(850, 800)[0] == 0:
            click(850, 800)
        if pyautogui.pixel(650, 800)[0] == 0:
            click(650, 800)

