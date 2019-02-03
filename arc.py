import turtle
import math

r = 100
arc = 180
fixedsides = 500
sides = arc * fixedsides // 360
length = 2 * math.pi * r / fixedsides
angle = 360/fixedsides
t = turtle.Turtle()
for i in range(sides):
    t.fd(length)
    t.lt(angle)