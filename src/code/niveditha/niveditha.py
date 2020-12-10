def main(t):
    t = t.Turtle()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()
    t.write("Niveditha")
    turtle.done()


if __name__ == '__main__':
    import turtle
    main(turtle)
