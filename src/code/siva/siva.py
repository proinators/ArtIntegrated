def snowflake(t, lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(t, lengthSide, levels - 1)
    t.left(60)
    snowflake(t, lengthSide, levels - 1)
    t.right(120)
    snowflake(t, lengthSide, levels - 1)
    t.left(60)
    snowflake(t, lengthSide, levels - 1)


def main(t):
    t.speed(0)
    length = 300.0
    t.penup()
    t.backward(length / 2.0)
    t.pendown()
    for i in range(3):
        snowflake(t, length, 4)
        t.right(120)
    t.mainloop()


if __name__ == '__main__':
    import turtle as tt
    main(tt)
