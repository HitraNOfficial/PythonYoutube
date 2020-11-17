import sys
import voice_handler as vh
import email_handler as eh
from time import sleep

engine = vh.init_engine()
voice = vh.get_voice(engine)
vh.speak("Hello, do you want to add groceries or send the list?", voice, engine)
choice = vh.get_audio()

print(choice)

if "add" in choice:
    vh.speak("Let me know what you want to add?", voice, engine)
    addition = vh.get_audio()
    print(addition)
    f = open("shooping_list.txt", "a")
    f.write(addition + "\n")
    f.close()
elif "send" in choice:
    vh.speak("Sending the current list to your email", voice, engine)
    with open ("shooping_list.txt", "r") as file:
        shopping_list = file.read()
        eh.email_alert('Shopping list', shopping_list)
else:
    vh.speak("Please restart me. I am still not that complicated", voice, engine)
    sys.exit()
