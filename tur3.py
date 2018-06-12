from turtle import Turtle
from random import randint

colors = ['red', 'blue', 'green', 'yellow']
pen = Turtle()
pen.speed(0)

def draw(radius = 50, angle = 90):
    pen.circle(radius)
    pen.left(angle)

for x in range(100):
    pen.color(colors[randint(0,3)])
    #pen.color(colors[x % 4])
    draw(radius = x, angle = 90)
