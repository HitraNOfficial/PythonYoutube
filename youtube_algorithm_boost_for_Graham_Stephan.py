import webbrowser
import pyautogui, time, sys

def booster():
    # like video
    pyautogui.moveTo(1030, 995, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    # scroll down
    pyautogui.scroll(-1000)

    # comment on video
    pyautogui.moveTo(180, 860, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)
    pyautogui.write('Greate video! Keep it up!', interval=0.2)
    pyautogui.moveTo(1300, 890, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    # scroll up
    pyautogui.scroll(1000)
    pyautogui.moveTo(1300, 950, 2, pyautogui.easeOutQuad)

webbrowser.open('https://www.youtube.com/channel/UCV6KDgJskWaEckne5aPA0aQ/videos')
time.sleep(2)
pyautogui.moveTo(500, 700, 2, pyautogui.easeOutQuad)
pyautogui.click(button='left', clicks=1)

try:
    while True:
        booster()
        time.sleep(60*15)

        # proceed to next video
        pyautogui.moveTo(75, 910, 2, pyautogui.easeOutQuad)
        pyautogui.click(button='left', clicks=1)
except KeyboardInterrupt:
    print('stopping...')
