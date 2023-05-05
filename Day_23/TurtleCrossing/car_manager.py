from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        create = randint(1, 6)
        if create == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            x = 300
            random_y = randint(-250, 250)
            new_car.goto(x, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
