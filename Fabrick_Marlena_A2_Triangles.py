# PROGRAMMER:  Marlena Fabrick
# PROGRAM NAME: Turtle Graphics — Triangles Design
# DATE WRITTEN: September 19, 2020
# PURPOSE:      Uses Python turtle graphics to draw three overlapping
#               triangles with concentric circles and a name label.

import turtle


def setup_screen():
    """Sets up the turtle screen."""
    screen = turtle.Screen()
    screen.bgcolor("cyan")
    screen.title("Triangles Graphic Design")
    return screen


def setup_pen():
    """Creates and configures the turtle pen."""
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(12)
    pen.width(5)
    pen.pencolor("green")
    return pen


def draw_triangle(pen, fill_color):
    """Draws a filled equilateral triangle."""
    pen.fillcolor(fill_color)
    pen.begin_fill()
    pen.forward(300)
    pen.left(120)
    pen.forward(300)
    pen.left(120)
    pen.forward(300)
    pen.end_fill()


def draw_circle(pen, x, y, radius, fill_color):
    """Draws a filled circle at the given screen position."""
    pen.fillcolor(fill_color)
    pen.begin_fill()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(radius)
    pen.end_fill()


def main():
    setup_screen()
    pen = setup_pen()

    # Draw three overlapping triangles
    draw_triangle(pen, "yellow")
    draw_triangle(pen, "yellow")
    draw_triangle(pen, "yellow")

    # Draw concentric circles
    draw_circle(pen, 0, -70,   100, "blue")
    draw_circle(pen, 0, -35,   50,  "violet")
    draw_circle(pen, 0, -18.5, 25,  "blue")

    pen.hideturtle()

    # Write name label
    pen.penup()
    pen.goto(-75, 0)
    pen.pendown()
    pen.pencolor("white")
    pen.write("Marlena G", font=("Times New Roman", 17, "bold"))

    turtle.done()


main()

