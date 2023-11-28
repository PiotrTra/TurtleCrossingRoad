from turtle import Screen
from player import Player

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Road")
screen.tracer(0)

player = Player()

game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")

while game_is_on:
    screen.update()



screen.exitonclick()
