def main(t):
    t.color('blue')
    t.write('NEERAJ BIJU!', font=('Courier', 20, 'italic'), align='left')
    t.hideturtle()

    n = int(input("Enter the no of sides:"))
    s = int(input("Enter the length of the side of the polygon: "))
    col = input("Enter the color name: ")

    t = t.Turtle()
    t.fillcolor(col)
    t.begin_fill()

    for i in range(n):
        t.forward(s)
        t.right(360 / n)

    t.end_fill()
    t.done()
    while True:
        t.hideturtle()


if __name__ == '__main__':
    import turtle
    main(turtle)
