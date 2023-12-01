from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-200, 270)
        self.ht()
        self.color("Black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("LeveL:  " + str(self.score), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_lvl(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
