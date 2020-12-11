def tree(length, n):
    if length > 5:
        n.forward(length)
        n.right(25)
        tree(length - 15, n)
        n.left(50)
        tree(length - 15, n)
        n.right(25)
        n.backward(length)


def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "eva":
            return
    data = t.Screen()
    data.clearscreen()
    data.setup(800, 600)
    data.tracer(0)
    t.ht()
    t.penup()
    t.goto(0, -200)
    t.write("By-Eva")
    n = t.Turtle()
    n.left(90)
    n.up()
    n.backward(100)
    n.down()
    n.pendown()
    n.color("Red")
    tree(100, n)
    data.update()
    # data.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
