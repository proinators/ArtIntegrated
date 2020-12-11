x_off = -400
y_off = -150
development = False
if development:
    from src.code.pratyush import pratyobj
else:
    from . import pratyobj


def tri(t, col, a, b, c):
    a = (a[0] + x_off, a[1] + y_off)
    b = (b[0] + x_off, b[1] + y_off)
    c = (c[0] + x_off, c[1] + y_off)
    t.colormode(1.0)
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
        if t.curr_program != "pratyush":
            return
    win = t.Screen()
    win.clearscreen()
    win.setup(800, 600)
    win.bgcolor("black")
    win.tracer(0)
    # win.title("PratyObj Rendering Engine (Turtle-based)")
    t.speed(0)
    t.pendown()

    data = pratyobj.read("sphere")

    tris = data["tris"]

    for i in tris:
        tri(t, *i)
    t.hideturtle()
    t.penup()
    t.setpos(-350, -250)
    t.write("By: " + data["author"], font=("Arial", 15, "normal"))
    win.update()
    #win.mainloop()


if __name__ == "__main__":
    import turtle
    main(turtle)
