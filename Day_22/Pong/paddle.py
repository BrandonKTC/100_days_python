from turtle import Turtle

PEACE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, coor: tuple) -> None:
        super().__init__()
        self.x = coor[0]
        self.y = coor[1]
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x, self.y)

    def up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def down(self):
        self.y -= 20
        self.goto(self.x, self.y)
