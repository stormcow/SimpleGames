from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level=0) -> None:
        self.level = level
        self.cars = []

    def spawnCars(self):
        Ycor = random.randint(-250, 250)
        newCar = Turtle(shape='square')
        newCar.color(random.choice(COLORS))
        newCar.penup()
        newCar.setpos(270, Ycor)
        newCar.setheading(180)
        newCar.shapesize(stretch_len=2)
        return newCar

    def increaseLevel(self):
        self.level += 1

    def addCars(self):
        if random.randint(0, 5) == 5:
            self.cars.append(self.spawnCars())

    def deleteCars(self):
        for index, car in enumerate(self.cars):
            if car.xcor < -300:
                self.cars.pop(index)

    def moveCars(self):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE + (self.level * MOVE_INCREMENT))
