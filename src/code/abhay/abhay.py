

x_off = -400
y_off = -150
turtle = None

def tri(col, a, b, c):
    a = (a[0] + x_off, a[1] + y_off)
    b = (b[0] + x_off, b[1] + y_off)
    c = (c[0] + x_off, c[1] + y_off)
    turtle.colormode(255)
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
    global turtle
    turtle = t
    dod = turtle.Screen()
    dod.clearscreen()
    dod.bgcolor("brown")
    dod.title("3D Cube")
    # dod.tracer(0)
    turtle.speed(0)
    turtle.penup()

    tris = [[(26, 26, 26), (369, 219), (499, 228), (438, 212)],
            [(97, 97, 97), (409, 348), (369, 219), (372, 295)],
            [(26, 26, 26), (369, 219), (410, 242), (499, 228)],
            [(194, 194, 194), (410, 242), (489, 317), (499, 228)],
            [(97, 97, 97), (409, 348), (410, 242), (369, 219)],
            [(194, 194, 194), (410, 242), (409, 348), (489, 317)]]

    for i in tris:
        tri(*i)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write(''' Abhay X A''', font=('Arial', 10, 'normal'))

    turtle.done()


if __name__ == '__main__':
    import turtle
    main(turtle)
