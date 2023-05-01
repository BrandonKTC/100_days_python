
from random import choice
from turtle import Turtle, colormode, Screen
import colorgram

# Picking the colors

extract_color = colorgram.extract("paint.jpg", 30)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extract_color]

# Drawing the hirst Painting
tim = Turtle()
tim.speed("fastest")

colormode(255)


def draw_line(num):
    for _ in range(num):
        tim.dot(20, choice(colors))
        tim.up()
        tim.forward(50)
        tim.down()


def painting(hor, ver):
    x = -300
    y = -300
    for _ in range(ver):
        tim.up()
        tim.goto(x, y)
        tim.down()
        draw_line(hor)
        y += 50


# painting(13, 11)

screen = Screen()
screen.exitonclick()
