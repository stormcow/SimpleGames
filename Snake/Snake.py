from turtle import Turtle


class Snake:

    def __init__(self, size=3) -> None:
        self.size = size
        self.body = []
        self.spawnSegments()

    def reset(self):
        for segment in self.body:
            segment.hideturtle()
        self.body.clear()
        self.spawnSegments()

    def spawnSegments(self):
        for i in range(self.size):
            newSegment = Turtle('square')
            newSegment.color('white')
            newSegment.penup()
            newSegment.setx(newSegment.xcor()-(i*20))
            self.body.append(newSegment)

    def extend(self):
        newPos = self.body[-1].position()
        newSegment = Turtle('square')
        newSegment.color('white')
        newSegment.penup()
        newSegment.setpos(newPos)
        self.body.append(newSegment)

    def moveForward(self):
        for segmentIndex in range(len(self.body)-1, 0, -1):
            newX = self.body[segmentIndex-1].xcor()
            newY = self.body[segmentIndex-1].ycor()
            self.body[segmentIndex].setpos(newX, newY)
        self.body[0].fd(20)

    def moveRight(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def moveLeft(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def moveUp(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def moveDown(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
