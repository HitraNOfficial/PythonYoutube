from turtle import Screen, Turtle
import voice_handler

screen = Screen()
screen.setup(width=1920, height=780, startx=0, starty=0)
turtle = Turtle()

engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak('Give command or say STOP to end the drawing phase?', voice, engine)

while True:
    voice_handler.speak('What angle?', voice, engine)
    command = voice_handler.get_audio()
    print(command)

    if 'stop' in command:
        break
    else:
        if command.isdigit():
            turtle.left(int(command))

        voice_handler.speak('What distance?', voice, engine)
        command = voice_handler.get_audio()
        print(command)
        if command.isdigit():
            turtle.forward(int(command))

screen.mainloop()
