
from random import choice
from turtle import Turtle, colormode, Screen
import colorgram

# Picking the colors

extract_color = colorgram.extract("paint.jpeg", 30)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extract_color]

# Drawing the hirst Painting
x = -225
y = -250

tim = Turtle()

colormode(255)


def draw_line(num):
    for _ in range(num):
        tim.dot(20, choice(colors))
        tim.up()
        tim.forward(50)
        tim.down()


for _ in range(10):
    tim.up()
    tim.goto(x, y)
    tim.down()
    draw_line(10)
    y += 50


screen = Screen()
screen.exitonclick()
