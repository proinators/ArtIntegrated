def main(t):
    #condition = lambda: True
    if hasattr(t, "curr_program"):
        if t.curr_program != "gouri":
            return
        #condition = lambda: t.curr_program == "gouri"
    s = t.Screen()
    s.clearscreen()
    s.setup(800, 600)
    s.tracer(0)
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    s.bgcolor('black')
    t.speed('fastest')
    t.pendown()
    t.hideturtle()
    for x in range(200):
        t.pencolor(colors[x % len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
    """while condition:
        for x in range(200):
            t.pencolor(colors[x % len(colors)])
            t.width(x / 100 + 1)
            t.forward(x)
            t.left(59)
        t.right(239)
        for x in range(200, 0, -1):
            t.pencolor('black')
            t.width(x / 100 + 7)
            t.forward(x)
            t.right(59)"""


if __name__ == '__main__':
    import turtle
    main(turtle)
