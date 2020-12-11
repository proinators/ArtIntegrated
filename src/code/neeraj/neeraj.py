def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "neeraj":
            return
    screen = t.Screen()
    screen.clearscreen()
    screen.setup(800, 600)
    screen.tracer(0)
    t.color('blue')
    t.write('NEERAJ BIJU!', font=('Courier', 20, 'italic'), align='left')
    t.home()
    t.pendown()
    t.hideturtle()

    n = int(input("Enter the no of sides: "))
    s = int(input("Enter the length of the side of the polygon: "))
    col = input("Enter the color name: ")

    t.fillcolor(col)
    t.begin_fill()

    for i in range(n):
        t.forward(s)
        t.right(360 / n)

    t.end_fill()
    t.hideturtle()
    screen.update()
    #screen.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
