from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-290, 290, 5)
        random_y = random.randrange(-290, 290, 5)
        # random_x = random.randint(-290, 290)
        # random_y = random.randint(-290, 290)
        self.setpos(random_x, random_y)
