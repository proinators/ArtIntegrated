import math
import colorsys


def main(ttl):
    ph = 180 * (3 - math.sqrt(5))
    ttl.speed(0)

    num = 200

    for x in reversed(range(0, num)):
        ttl.fillcolor(colorsys.hsv_to_rgb(x / num, 1.0, 1.0))
        ttl.begin_fill()
        ttl.circle(5 + x, None, 11)
        ttl.end_fill()
        ttl.right(ph)
        ttl.right(.8)

    ttl.mainloop()


if __name__ == '__main__':
    import turtle
    main(turtle)
