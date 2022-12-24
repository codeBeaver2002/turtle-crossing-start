from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)
