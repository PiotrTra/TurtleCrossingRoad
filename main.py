from turtle import Screen

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossing Road")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()



screen.exitonclick()
