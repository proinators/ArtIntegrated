x_off = -400
y_off = -150
development = True
if development:
    from src.code.pratyush import pratyobj
else:
    import pratyobj


def tri(turtle, col, a, b, c):
    a = (a[0] + x_off, a[1] + y_off)
    b = (b[0] + x_off, b[1] + y_off)
    c = (c[0] + x_off, c[1] + y_off)
    turtle.colormode(1.0)
    turtle.fillcolor(*col)
    turtle.pencolor(*col)
    turtle.penup()
    turtle.goto(*a)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(*b)
    turtle.goto(*c)
    turtle.goto(*a)
    turtle.end_fill()


def main(t):
    win = t.Screen()
    win.clearscreen()
    win.setup(800, 600)
    win.bgcolor("black")
    #win.title("PratyObj Rendering Engine (Turtle-based)")
    t.speed(0)

    data = pratyobj.read("sphere")

    tris = data["tris"]

    for i in tris:
        tri(t, *i)
    t.hideturtle()
    t.penup()
    t.setpos(-350, -250)
    t.write("By: " + data["author"], font=("Arial", 15, "normal"))
    t.mainloop()


if __name__ == "__main__":
    import turtle as tt
    main(tt)
