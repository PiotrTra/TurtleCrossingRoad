import time
from turtle import Turtle
import random

CARS_COLORS = ["yellow", "green", "blue", "pink", "black", "purple", "orange"]
STARTING_X = 290


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.ht()
        self.cars = []
        self.random_y = 0
        self.random_color = None

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        self.random_color = random.choice(CARS_COLORS)
        self.random_y = random.randint(-240, 240)
        new_car.color(self.random_color)
        new_car.goto(STARTING_X, self.random_y)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def increase_speed(self):
        self.speed += 10
