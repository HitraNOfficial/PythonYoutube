import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voice = get_voice(engine)
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

def get_voice(engine):
    voices = engine.getProperty('voices')

    #Windows
    for voice in voices:
        if 'David' in voice.name:
            desired_voice = voice
            break
    
    return desired_voice
