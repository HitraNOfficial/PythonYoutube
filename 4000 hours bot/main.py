import subprocess
import pyautogui
import time
from PIL import ImageGrab  # screenshot
import pytesseract
from pytesseract import Output


def open_tor():
    # careful about the / when you it's usually \
    subprocess.Popen(["D:/Tor Browser/Browser/firefox.exe"],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    time.sleep(10)  # to give plenty of time for Tor to load


def quit_tor():
    pyautogui.click(x=980, y=30)


def play_playlist():
    pyautogui.click(x=300, y=80)
    pyautogui.typewrite(
        'https://youtu.be/eTljKIvg3Ho?si=P0Vh5I3oQVsG3DU')
    pyautogui.press('enter')
    time.sleep(20)  # for loading of video
    pyautogui.press('space')  # start the video


def check_accept(data):
    if 'Before you continue' in data:
        pyautogui.click(x=770, y=890)


def anti_bot(data, reset):
    if 'google.com' in data or reset is True:
        quit_tor()
        time.sleep(2)
        open_tor()
        play_playlist()
        check_accept(data)


if __name__ == '__main__':
    hard_reset = 0

    open_tor()
    play_playlist()

    # needed for Windows as OS instead of env. variable
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract")

    # just set the value in range 60 * the amount of hours
    # Example 60 * 10 = 600 (will run for 10 hours)
    for increments in range(600):
        screen = ImageGrab.grab()  # screenshot
        cap = screen.convert('L')  # make it grayscale

        data = pytesseract.image_to_string(cap)

        check_accept(data)
        anti_bot(data, False)
        time.sleep(60)  # do this every 60 seconds to go easy on your PC

        hard_reset += 1
        if (hard_reset >= 60):  # reset every hour to simulate many viewers
            anti_bot(data, True)
            hard_reset = 0
