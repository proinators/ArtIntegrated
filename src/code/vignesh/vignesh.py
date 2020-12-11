import math
import colorsys


def main(t):
    screen = t.Screen()
    screen.clearscreen()
    screen.setup(800, 600)
    screen.tracer(0)
    if hasattr(t, "curr_program"):
        if t.curr_program != "vignesh":
            return
    ph = 180 * (3 - math.sqrt(5))
    t.speed(0)
    t.pendown()

    num = 200

    for x in reversed(range(0, num)):
        t.fillcolor(colorsys.hsv_to_rgb(x / num, 1.0, 1.0))
        t.begin_fill()
        t.circle(5 + x, None, 11)
        t.end_fill()
        t.right(ph)
        t.right(.8)
    screen.update()
    #screen.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
