x_off = -400
y_off = -150


def tri(t, col, a, b, c):
    a = (a[0] + x_off, a[1] + y_off)
    b = (b[0] + x_off, b[1] + y_off)
    c = (c[0] + x_off, c[1] + y_off)
    t.colormode(255)
    t.fillcolor(*col)
    t.pencolor(*col)
    t.penup()
    t.goto(*a)
    t.pendown()
    t.begin_fill()
    t.goto(*b)
    t.goto(*c)
    t.goto(*a)
    t.end_fill()


def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "abhay":
            return
    dod = t.Screen()
    dod.setup(800, 600)
    dod.clearscreen()
    dod.bgcolor("brown")
    dod.tracer(0)
    t.speed(0)
    t.penup()

    tris = [[(26, 26, 26), (369, 219), (499, 228), (438, 212)],
            [(97, 97, 97), (409, 348), (369, 219), (372, 295)],
            [(26, 26, 26), (369, 219), (410, 242), (499, 228)],
            [(194, 194, 194), (410, 242), (489, 317), (499, 228)],
            [(97, 97, 97), (409, 348), (410, 242), (369, 219)],
            [(194, 194, 194), (410, 242), (409, 348), (489, 317)]]

    for i in tris:
        tri(t, *i)
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.write(''' Abhay X A''', font=('Arial', 10, 'normal'))
    dod.update()
    # dod.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
