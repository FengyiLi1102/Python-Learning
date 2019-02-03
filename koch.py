import turtle

def koch(t, n):
    if n < 10:
        t.fd(n)
        return
    m = n / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

a = turtle.Turtle()

for i in range(3):
    koch(a, 20)
    a.rt(120)
turtle.mainloop()
