from turtle import Turtle

SCORE = 0
FONT = ('courier', 25, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.goto(-20, 270)
        self.ht()
        self.show_score()

    def increase_score(self):
        self.clear()
        self.show_score()
        self.score += 1

    def show_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
