from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.x_velocity = 1
        self.y_velocity = 3
        self.refresh()

    def move(self):
        self.checkBoundries()
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)

    def checkBoundries(self):
        if self.xcor() <= -380 or self.xcor() >= 380:
            self.x_velocity *= -1
            self.refresh()
        if self.ycor() <= -280 or self.ycor() >= 280:
            self.y_velocity *= -1

    # def checkLose(self):
        # if self.xcor() <=

    def checkPaddle(self, paddle1, paddle2):
        # print(self.distance(paddle))
        if (self.xcor() <= -330 and self.distance(paddle1) < 60) or (self.xcor() >= 330 and self.distance(paddle2) < 60):
            if self.x_velocity < 0:
                self.x_velocity -= 0.1
            elif self.x_velocity >= 0:
                self.x_velocity += 0.1
            self.x_velocity *= -1

    def refresh(self):
        randomY = random.randint(-250, 250)
        self.x_velocity = 1
        self.setpos(0, randomY)
        self.shape('circle')
        self.color('white')
        self.penup()
