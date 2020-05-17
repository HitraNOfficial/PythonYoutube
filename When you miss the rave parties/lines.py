import turtle
import time, sys

STAMP_SIZE = 3

def lines(my_turtle, length, reps, separation):
    separation += 1

    my_stamp = my_turtle.clone()
    my_stamp.shape('square')
    my_stamp.shapesize(1 / STAMP_SIZE, length / STAMP_SIZE, 0)
    my_stamp.tilt(-30)
    my_stamp.penup()
    my_stamp.left(90)
    my_stamp.backward((reps - 1) * separation / 2)
    my_stamp.fillcolor('lime')

    for _ in range(reps):
        my_stamp.stamp()
        my_stamp.forward(separation)
        my_stamp.tilt(reps * 10 - 30)
    
    my_stamp.hideturtle()

wn = turtle.Screen()
wn.setup(width=0.99, height=0.99)

t = turtle.Turtle()
t.hideturtle()

for x in range(0, 100):
    wn.bgcolor('black')
    t.pencolor('lime')
    lines(t.getturtle(), 250, 25, 30)
    turtle.resetscreen()
    time.sleep(0.1)

turtle.done()

# for the error
# https://www.reddit.com/r/vscode/comments/b6a2p2/red_underline/
