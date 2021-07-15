import pyautogui as gui
import keyboard
import time

# GAME LINK --> https://www.addictinggames.com/shooting/storm-the-house#url
# Screen Dimensions for screen of size 1920X1080
top, left, width, height = 0, 0, 500, 520

mag_size = 7
enemy_color = (0, 0, 0)
day = 1
start_time = time.time()


def destroy_them():
    global mag_size, day

    screenshot = gui.screenshot(region=(left, top, width, height))
    pixels = screenshot.load()

    for x in reversed(range(0, 500)):
        if mag_size <= 0:
            gui.keyDown('space')
            mag_size = 7
            time.sleep(0.8)
            gui.keyUp('space')
            break

        for y in reversed(range(400, 520)):
            # dirty fix for rogue tank to avoid clicking the gunman button
            if (y < 420 and x < 85):
                break

            if pixels[x, y] == enemy_color:
                gui.click(x=x, y=y, clicks=2)
                mag_size -= 2
                y += 20

            if mag_size <= 0:
                break


def buy_gunman():
    gui.click(x=60, y=400, clicks=10)


def buy_defences():
    gui.click(x=425, y=235, clicks=1)
    gui.click(x=140, y=400, clicks=4)


def next():
    gui.click(x=315, y=530)


while True:

    if keyboard.is_pressed('q'):  # Emergency Button
        break

    destroy_them()

    if ((time.time() - start_time) >= 100):
        print('End of day ' + str(day))
        day += 1
        if (day > 14):
            buy_gunman()
        elif (day == 14):
            buy_defences()

        start_time = time.time()
        next()
