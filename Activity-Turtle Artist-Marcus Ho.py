# Turtle Artist
# Author:
# 28 October

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
artist = turtle.Turtle()
artist.speed(5)

# Variables for positioning and sizing
house_x = -100
house_y = -150
house_width = 200
house_height = 150
window_size = 40
door_width = 40
door_height = 70


def draw_rectangle(width, height, color):
    """Draw a filled rectangle with given dimensions and color"""
    artist.fillcolor(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()


def draw_window(size, color):
    """Draw a window with cross pattern"""
    # Draw window frame
    draw_rectangle(size, size, color)

    # Draw cross lines
    artist.pencolor("white")
    artist.pensize(2)

    # Vertical line
    artist.penup()
    artist.forward(size / 2)
    artist.pendown()
    artist.left(90)
    artist.forward(size)

    # Horizontal line
    artist.penup()
    artist.right(90)
    artist.backward(size / 2)
    artist.pendown()
    artist.forward(size)

    # Reset
    artist.penup()
    artist.backward(size / 2)
    artist.right(90)
    artist.forward(size / 2)
    artist.pensize(1)
    artist.pencolor("black")


def draw_door(width, height, color):
    """Draw a door with a doorknob"""
    draw_rectangle(width, height, color)

    # Draw doorknob
    artist.penup()
    artist.forward(width * 0.75)
    artist.left(90)
    artist.forward(height / 2)
    artist.pendown()
    artist.dot(5, "gold")

    # Reset position
    artist.penup()
    artist.backward(height / 2)
    artist.right(90)
    artist.backward(width * 0.75)


def draw_triangle_roof(base, color):
    """Draw a triangular roof"""
    artist.fillcolor(color)
    artist.begin_fill()
    artist.forward(base)
    artist.left(120)
    artist.forward(base)
    artist.left(120)
    artist.forward(base)
    artist.left(120)
    artist.end_fill()


def draw_sun(x, y, radius, color):
    """Draw a sun with rays"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()

    # Draw sun circle
    artist.fillcolor(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

    # Draw sun rays
    artist.penup()
    artist.goto(x, y + radius)
    artist.pendown()
    artist.pencolor("yellow")
    artist.pensize(3)

    for _ in range(12):
        artist.forward(20)
        artist.backward(20)
        artist.right(30)

    artist.pensize(1)
    artist.pencolor("black")


def draw_grass_blades(x, y, num_blades):
    """Draw multiple grass blades"""
    for i in range(num_blades):
        artist.penup()
        artist.goto(x + i * 15, y)
        artist.pendown()
        artist.pencolor("darkgreen")
        artist.pensize(2)
        artist.setheading(90)
        artist.forward(15)
        artist.backward(15)
    artist.pensize(1)
    artist.pencolor("black")


# Draw grass ground
artist.penup()
artist.goto(-400, -150)
artist.pendown()
draw_rectangle(800, 100, "green")

# Draw grass blades
draw_grass_blades(-350, -150, 30)

# Draw house base
artist.penup()
artist.goto(house_x, house_y)
artist.pendown()
artist.setheading(0)
draw_rectangle(house_width, house_height, "lightcoral")

# Draw roof
artist.penup()
artist.goto(house_x, house_y + house_height)
artist.pendown()
draw_triangle_roof(house_width, "darkred")

# Draw left window
artist.penup()
artist.goto(house_x + 25, house_y + 80)
artist.pendown()
artist.setheading(0)
draw_window(window_size, "lightblue")

# Draw right window
artist.penup()
artist.goto(house_x + 135, house_y + 80)
artist.pendown()
artist.setheading(0)
draw_window(window_size, "lightblue")

# Draw door
artist.penup()
artist.goto(house_x + 80, house_y)
artist.pendown()
artist.setheading(0)
draw_door(door_width, door_height, "brown")

# Draw sun
draw_sun(150, 150, 30, "yellow")

# Hide turtle and display
artist.hideturtle()
turtle.done()
