import turtle

def draw_koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)
        t.right(120)
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)


if __name__ == "__main__":
    level = int(input("Enter the level of recursion: "))
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    for i in range(3):
        draw_koch_snowflake(t, 300, level)
        t.right(120)

    screen.mainloop()