from turtle import Turtle

def drawCircle(n):
    pen = Turtle()
    pen.speed(0)
    pen.color('blue')
    for x in range(n):
        pen.circle(50)
        pen.left(360/n)


drawCircle(20)
