import sys
import voice_handler
from time import sleep

def ask_question(line):
    currentQuestion = line.split("|")
    print(currentQuestion)
    for i in range(0, 4):
        voice_handler.speak(currentQuestion[i], voice, engine)
    
    # you need to wait a second before answering
    currentAnswer = voice_handler.get_audio()
    print(currentAnswer)

    if currentQuestion[4] in currentAnswer:
        voice_handler.speak("Correct!", voice, engine)
    else:
        voice_handler.speak("Wrong! The correct answer is: " + currentQuestion[4], voice, engine)


engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak("Get ready to revise!", voice, engine)

with open("quiz.txt") as file_in:
    for line in file_in:
        ask_question(line)
        sleep(60)
