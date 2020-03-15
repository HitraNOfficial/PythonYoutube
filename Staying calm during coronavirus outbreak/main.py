import sys, time, voice_handler, webbrowser
from PIL import Image

engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak('Stay calm during coronavirus outbreak!', voice, engine)

calming_dictionary = {}
with open("calming_dictionary.txt") as f:
    for line in f:
       (key, val) = line.split(' : ')
       calming_dictionary[key] = val

try:
    for key, value in calming_dictionary.items():
        if "video" in key:
            webbrowser.open(value)
        else:
            img = Image.open(key)
            img.show()
            voice_handler.speak(value, voice, engine)
        time.sleep(15)
except KeyboardInterrupt:
    print('stopping...')
