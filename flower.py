import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def move2(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)
    turtle.mainloop()

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()
alice = turtle.Turtle()

#move(bob, -100)
#move2(bob, 7, 60, 60)

move(alice, 50)
move2(alice, 10, 60, 60)


