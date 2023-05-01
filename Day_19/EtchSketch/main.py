from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def clear():
    tim.clear()
    tim.up()
    tim.goto(0, 0)
    tim.down()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
