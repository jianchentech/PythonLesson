import turtle
pen = turtle.Pen()
pen.speed(0)
colors = ['red', 'green', 'blue', 'pink']
for i in range(300):
    pen.pencolor(colors[i % 4])
    pen.forward(2*i)
    pen.left(91)
turtle.done()

