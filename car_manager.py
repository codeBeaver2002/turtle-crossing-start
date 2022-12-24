import time
from random import *
from turtle import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def generate(self):
        random_chance = randint(1,20)
        if random_chance == 1:
            turtles = Turtle()
            turtles.shape("square")
            turtles.penup()
            turtles.goto(280, randint(-260, 280))
            turtles.shapesize(stretch_wid=1, stretch_len=2)
            turtles.color(choice(COLORS))
            self.all_cars.append(turtles)


    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)
