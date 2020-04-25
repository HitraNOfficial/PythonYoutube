import webbrowser
import pyautogui, time, sys

def join_meeting(meetingId, duration):
    pyautogui.moveTo(1250, 1060, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    time.sleep(2)
    webbrowser.open(meetingId)

    time.sleep(2)
    pyautogui.moveTo(980, 680, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    # only for zoom test meetings sequence
    time.sleep(4)
    pyautogui.moveTo(520, 580, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)
    time.sleep(0.5)
    pyautogui.click(button='left', clicks=1)
    pyautogui.moveTo(570, 680, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)
    # end of test meeting sequence

    time.sleep(2)
    pyautogui.moveTo(960, 470, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    stay_online(duration)

    pyautogui.moveTo(1510, 800, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    time.sleep(1)
    pyautogui.moveTo(1000, 590, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

    time.sleep(1)
    pyautogui.moveTo(1230, 330, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=1)

def stay_online(duration):
    try:
        while duration >= 0:
            time.sleep(30)
            pyautogui.moveTo(500, 500, 2, pyautogui.easeOutQuad)
            pyautogui.moveTo(1000, 1000, 2, pyautogui.easeOutQuad)
            duration = duration - 30
    except KeyboardInterrupt:
        print('stopping...')