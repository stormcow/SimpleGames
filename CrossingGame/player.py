from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape='turtle')
        self.refresh()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def refresh(self):
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.speed('fastest')

    def checkWin(self):
        if self.ycor() > FINISH_LINE_Y:
            self.refresh()
            return True
        else:
            return False

    def checkLose(self, cars):
        for car in cars:
            if self.distance(car) < 15:
                return True
