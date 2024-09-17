from turtle import*


def triangle():
    speed(50)
    pensize(15)
    color("light blue")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    exitonclick()

def polygon():
    speed(50)
    pensize(15)
    color("GreenYellow")
    for i in range(5):
        forward(100)
        left(72)
    hideturtle()
    exitonclick()


def mountains():
    speed(50)
    penup()
    goto(-200, 0)
    pendown()
    pensize(10)


    for i in range(4):
        color("indigo")
        left(70)
        forward(50)
        right(140)
        forward(50)
        left(140)
        color("thistle")
        forward(100)
        right(140)
        forward(100)
        left(70)

    hideturtle()
    exitonclick()

def _treugolnic():
    pensize(2)
    color("blue")
    for i in range(3):
        forward(100)
        left(120)


def cirkel():
    speed(50)
    for i in range(36):
        _treugolnic()
        left(10)
    hideturtle()
    exitonclick()


def flower():
    pensize(2)
    speed(50)
    color("Gold")
    size = 10
    for i in range(7):
        circle(size)
        size += 10
    left(90)
    size = 10
    for i in range(7):
        circle(size)
        size += 10
    left(90)
    size = 10
    for i in range(7):
        circle(size)
        size += 10
    left(90)
    size = 10
    for i in range(7):
        circle(size)
        size += 10
    exitonclick()


def __scwuar(size, color_q):
    pensize(2)
    color(color_q)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()

def plitcka():
    penup()
    goto(-50, -50)
    pendown()
    s = "black"
    d = "white"
    l = "lavender"
    w = 200
    f = 150
    k = 100
    g = 50
    __scwuar(w, s)
    __scwuar(f, d)
    __scwuar(k, l)
    __scwuar(g, s)
    hideturtle()
    exitonclick()


