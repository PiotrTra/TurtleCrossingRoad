from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Road")
screen.tracer(0)

player = Player()
car = Car()

game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")

while game_is_on:
    car.move_car()
    time.sleep(1)
    car.create_car()
    screen.update()

screen.exitonclick()
