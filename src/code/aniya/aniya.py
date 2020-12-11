def drawRightArc(t, degrees):
    for i in range(degrees):
        t.forward(1)
        t.right(1)


def drawLeftArc(t, degrees):
    for i in range(degrees):
        t.forward(1)
        t.left(1)


def drawRay(t):
    for i in range(2):
        drawLeftArc(t, 90)
        drawRightArc(t, 90)


def drawSun(t):
    for i in range(9):
        drawRay(t)
        t.right(160)


def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "aniya":
            return
    screen = t.Screen()
    screen.clearscreen()
    screen.setup(800, 600)
    screen.bgcolor("lightblue")
    screen.tracer(0)

    t.color("black")
    t.fillcolor("orange")
    t.width(1)
    # t.speed(0)

    t.penup()
    t.goto(-125, -100)
    t.pendown()

    t.begin_fill()
    drawSun(t)
    t.end_fill()
    t.write("Aniya")

    screen.update()
    # screen.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
