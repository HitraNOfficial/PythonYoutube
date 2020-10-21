import pyautogui
from mss import mss
import time
import keyboard

start_x = 800
start_y = 550
gap_y = 80

bbox = (start_x, start_y, start_x + 400, start_y + gap_y)
coordX = [0, 100, 200, 300]

sleeping_time = 0.065

time.sleep(1)
with mss() as sct:
    while True:
        if keyboard.is_pressed('q'): # Emergency exit
            break

        img = sct.grab(bbox)
        for current_y in reversed(range(0, gap_y)):
            if (img.pixel(coordX[0], current_y)[0] == 17):
                pyautogui.press('a')
                time.sleep(sleeping_time)
                break

            if (img.pixel(coordX[1], current_y)[0] == 17):
                pyautogui.press('s')
                time.sleep(sleeping_time)
                break

            if (img.pixel(coordX[2], current_y)[0] == 17):
                pyautogui.press('d')
                time.sleep(sleeping_time)
                break

            if (img.pixel(coordX[3], current_y)[0] == 17):
                pyautogui.press('f')
                time.sleep(sleeping_time)
                break
