from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)
