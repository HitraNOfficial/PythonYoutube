import pyttsx3

def init_engine():
    return pyttsx3.init()

def speak(text, voice, engine):
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 130) # Speed percent can go over 100
    engine.say(text)
    engine.runAndWait()

def get_voice(engine):
    voices = engine.getProperty('voices')
    # Windows voice check (for Mac first call check_all_voices)
    # and choose a proper voice that you like
    for voice in voices:
        if "Zira" in voice.name:
            desired_voice = voice
            break

    return desired_voice
