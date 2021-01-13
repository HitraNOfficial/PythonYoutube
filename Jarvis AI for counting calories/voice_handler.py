import os
import time
import speech_recognition as sr
import pyttsx3

def init_engine():
    return pyttsx3.init()

def check_all_voices(engine):
    voices = engine.getProperty('voices')
    for voice in voices:
        print("Voice:")
        print(" - ID: %s" % voice.id)
        print(" - Name: %s" % voice.name)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)

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

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # this gives a little delay but handles ambient noise
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except sr.RequestError:
            print("API was unreachable or unresponsive")
        except sr.UnknownValueError:
            print("Unable to recognize speech")

    return said
