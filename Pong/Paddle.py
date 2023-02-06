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
        self.y_velocity = 50

        self.y_target = 0

    def update(self):
        self.sety(lerp(self.ycor(), self.y_target, 0.1))

    def moveForward(self):
        if self.ycor() <= 200:
            self.y_target = self.ycor() + self.y_velocity

    def moveBack(self):
        if self.ycor() >= -200:
            self.y_target = self.ycor() - self.y_velocity


def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b