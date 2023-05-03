from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()


screen.setup(width=800, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.onkey(key="s", fun=l_paddle.up)
screen.onkey(key="w", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

game_is_on = True


# def game(game_is_on):
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        print("l_paddle scores")
        scoreboard.scores("l")
        ball.reset_position()

    elif ball.xcor() < -380:
        print("r_paddle scores")
        scoreboard.scores()
        ball.reset_position()


# while play[0] != "n":
#     play = input("Play again ? (yes or no): ").lower()
#     if play[0] == "y":
#         game(True)
#     elif play[0] == "n":
#         game(False)

screen.exitonclick()
