def main(t):
    s = t.Screen()
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    s.bgcolor('black')
    t.speed('fastest')
    t.hideturtle()
    while True:
        for x in range(200):
            t.pencolor(colors[x % len(colors)])
            t.width(x / 100 + 1)
            t.forward(x)
            t.left(59)
        t.right(239)
        for x in range(200, 0, -1):
            t.pencolor('black')
            t.width(x / 100 + 7)
            t.forward(x)
            t.right(59)


if __name__ == '__main__':
    import turtle
    main(turtle)
