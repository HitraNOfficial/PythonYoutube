from turtle import Screen, Turtle
import time
import turtle

screen = Screen()
screen.bgcolor('light pink')
screen.setup(width=1920, height=1080, startx=0, starty=0)

time.sleep(2)

turtle = Turtle()
turtle.hideturtle()
turtle.color('purple')
turtle.begin_fill()
turtle.fillcolor('purple')
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)
turtle.setheading(60)
turtle.circle(-90, 200)
turtle.forward(180)
turtle.end_fill()

turtle.sety(-100)
turtle.color('deep pink')
style = ('Courier', 50, 'italic')
turtle.write('Happy Birthday DEEKSHITA, font=style, align='center')

screen.mainloop()
