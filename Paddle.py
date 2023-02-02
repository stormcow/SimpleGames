from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos=350) -> None:
        super().__init__()
        self.shape('square')
        self.turtlesize(1, 5)
        self.setheading(90)
        self.penup()
        self.color('white')
        self.setx(pos)
        self.speed('fastest')
        self.y_velocity = 10

    def moveForward(self):
        if self.ycor() <= 200:
            self.sety(self.ycor() + self.y_velocity)

    def moveBack(self):
        if self.ycor() >= -200:
            self.sety(self.ycor() - self.y_velocity)
