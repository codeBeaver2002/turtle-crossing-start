import time
from turtle import Screen
from player import *
from car_manager import *
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
screen.listen()
screen.onkeypress(turtle.move, "w")

blocks = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.001)
    if turtle.ycor() == 280:
        score.update()
        turtle.starting_position()
        blocks.speed += 0.5
    for car in blocks.all_cars:
        if car.distance(turtle) < 20:
            score.clear()
            score.goto(0,0)
            score.write(f"Game Over.\nMax Score: {score.score}", align="center", font=FONT)
            screen.exitonclick()
    blocks.generate()
    blocks.move()
    screen.update()