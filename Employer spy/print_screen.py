import pyautogui
import time
from datetime import datetime

while True:
    now = datetime.timestamp(datetime.now())
    screenshot = pyautogui.screenshot(str(now) + '.png')
    time.sleep(30)
