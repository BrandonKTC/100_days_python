from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
