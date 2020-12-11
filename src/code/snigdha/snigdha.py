def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "snigdha":
            return
    s = t.Screen()
    s.clearscreen()
    s.setup(800, 600)
    s.tracer(0)
    t.shape("arrow")
    t.color("#a86f14")
    t.fillcolor("#efb456")
    t.pensize(2)
    t.delay(10)
    t.pendown()
    for j in range(6):
        t.penup()
        t.forward(28)
        t.left(90)
        t.forward(21)
        t.right(90)
        t.pendown()
        t.begin_fill()
        for i in range(6):
            t.forward(20)
            t.left(60)
        t.end_fill()
    t.hideturtle()
    s.update()
    #s.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
