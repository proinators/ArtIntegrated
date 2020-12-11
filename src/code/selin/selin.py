def draw_square(t):
    t.begin_fill()
    for side in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "selin":
            return
    screen = t.Screen()
    screen.clearscreen()
    screen.setup(500, 500)
    screen.bgcolor("black")
    screen.tracer(0)

    t.color("red")
    t.pendown()
    t.speed(0)
    t.width(3)
    t.hideturtle()

    t.penup()
    t.goto(-350, 0)
    t.pendown()

    for i in range(-25000, 35000, 12):
        t.clear()
        draw_square(t)
        screen.update()
        t.forward(0.12)
    #screen.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
