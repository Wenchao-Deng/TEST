from turtle import Turtle

def drawCircle(n):
    pen = Turtle()
    pen.speed(0)
    pen.color('blue')
    for x in range(100):
        pen.circle(x)
        pen.left(360/n)

drawCircle(6)
