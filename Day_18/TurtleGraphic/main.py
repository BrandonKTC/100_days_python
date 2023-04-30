from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
colormode(255)

tim.speed('fastest')
tim.shape("turtle")

# Challenge #1


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)

# Challenge #2


def dash_line(steps):
    for _ in range(steps):
        tim.down()
        tim.forward(50)
        tim.up()
        tim.forward(50)

# Challenge #3


def different_shape(num):
    for i in range(3, num):
        tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        for _ in range(i):
            tim.forward(100)
            tim.right(360/i)

# Challenge #4


def random_walk():
    while True:
        tim.pensize(10)
        tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        heads = randint(0, 1)
        if heads == 0:
            tim.left(90)
        else:
            tim.right(90)
        tim.forward(25)

# Challenge #5


def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        tim.circle(100)
        tim.right(size)


screen = Screen()
screen.exitonclick()
