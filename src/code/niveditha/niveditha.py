def main(t):
    if hasattr(t, "curr_program"):
        if t.curr_program != "niveditha":
            return
    s = t.Screen()
    s.clearscreen()
    s.setup(800, 600)
    s.tracer(0)
    t.fillcolor("red")
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()
    t.write("Niveditha")
    s.update()
    #s.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
