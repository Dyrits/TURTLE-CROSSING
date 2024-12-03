from random import choices, randint
from turtle import Turtle

STARTING_MOVE_DISTANCE = {
    "green": 1,
    "blue": 2,
    "purple": 4,
    "yellow": 8,
    "orange": 16,
    "red": 32,
}

MOVE_INCREMENT = 1

FREQUENCIES = {
    "green": 4096,
    "blue": 1024,
    "purple": 256,
    "yellow": 64,
    "orange": 16,
    "red": 4,
}

MAX_CARS = 16  # Maximum number of cars allowed on the screen at once

class Garage:
    increment = 0

    def __init__(self):
        self.cars = []

    def create_car(self):
        if len(self.cars) < MAX_CARS and randint(1, 4) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # Get random card based on frequency:
            color = choices(list(FREQUENCIES.keys()), weights=FREQUENCIES.values())[0]
            car.color(color)
            car.speed = MOVE_INCREMENT * self.increment + STARTING_MOVE_DISTANCE[color]
            y = randint(-250, 250)
            while not all(abs(y - existing_car.ycor()) > 20 for existing_car in self.cars):
                y = randint(-250, 250)
            car.goto(300, y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(car.speed)
        self.cars = [car for car in self.cars if car.xcor() > -320]

    def speed_up(self):
        self.increment += 1
        for car in self.cars:
            car.speed += MOVE_INCREMENT
