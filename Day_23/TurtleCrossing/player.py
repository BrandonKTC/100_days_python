from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting()
        self.seth(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def starting(self):
        self.goto(STARTING_POSITION)
