import turtle
import time, sys
from playsound import playsound

playsound('audio.mp3', 0) # run in background

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=0.99, height=0.99)

for x in range(0, 1000):
    if x % 2 == 0:
        wn.bgcolor("red")
    else:
        wn.bgcolor("white")
    
    time.sleep(0.15)

turtle.done()