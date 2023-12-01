from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Road")
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")

while game_is_on:
    number_to_create_car = random.randint(0, 50)
    car.move_car()
    time.sleep(0.1)
    if number_to_create_car % 2 == 0 and number_to_create_car % 3 == 0:
        car.create_car()
        screen.update()
    for auto in car.cars:
        # Detect collision with car
        if player.distance(auto) < 25:
            scoreboard.game_over()
            game_is_on = False
    # Detect completing the lvl
    if player.ycor() == 280:
        scoreboard.increase_lvl()
        player.restart()
        car.increase_speed()
    screen.update()

screen.exitonclick()
