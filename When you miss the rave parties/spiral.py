import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 0.99, height= 0.99)

t = turtle.Turtle()
angle = 91
t.showturtle()
t.shape("turtle")
t.pencolor("red")

for x in range(1000):
    t.forward(x)
    t.left(angle)

turtle.done()
