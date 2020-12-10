turtle = None


def tree(Length, n):
    if Length > 5:
        n.forward(Length)
        n.right(25)
        tree(Length - 15, n)
        n.left(50)
        tree(Length - 15, n)
        n.right(25)
        n.backward(Length)


def main(t):
    t.ht()
    t.penup()
    t.goto(0, -200)
    t.write("By-Eva")
    n = t.Turtle()
    data = t.Screen()
    n.left(90)
    n.up()
    n.backward(100)
    n.down()
    n.color("Red")
    tree(100, n)
    data.exitonclick()


if __name__ == '__main__':
    import turtle
    main(turtle)
