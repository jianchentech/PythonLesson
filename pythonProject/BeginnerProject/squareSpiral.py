## The project was built based on Turtle
import turtle
pen = turtle.Pen()
pen.speed(0)
pen.pencolor('green')
for i in range(200):
    if i%2==0:
        pen.pencolor('red')
    elif i%3==0:
        pen.pencolor('green')
    else:
        pen.pencolor('blue')
    pen.forward(2*i)
    pen.left(90)

turtle.done()

