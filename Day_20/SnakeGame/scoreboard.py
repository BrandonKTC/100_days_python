from turtle import Turtle

SCORE = 0
FONT = ('courier', 25, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.high_score()
        self.color("white")
        self.up()
        self.goto(-20, 270)
        self.ht()
        self.update_scoreboard()

    def high_score(self):
        with open("./data.txt", mode="r") as f:
            return int(f.read())

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as f:
                f.write(str(self.high_score))
            f.close()
        self.score = 0
        self.update_scoreboard()
