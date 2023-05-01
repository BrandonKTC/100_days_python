from turtle import Turtle, Screen
from random import randint

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? ENter a color: ")

x = -230
y = -50

all_turtles = []

for i, color in enumerate(colors):
    t = Turtle("turtle")
    t.up()
    t.color(color)
    t.goto(x, y)
    all_turtles.append(t)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
