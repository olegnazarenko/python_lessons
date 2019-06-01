# https://docs.python.org/2/library/turtle.html#turtle.dot
# https://michael0x2a.com/blog/turtle-examples

import turtle

ninja = turtle.Turtle()

ninja.speed(1000)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(80)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()