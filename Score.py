from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.p1Score = 0
        self.p2Score = 0
        self.writeScore()

    def updateP1Score(self):
        self.p1Score += 1

    def updateP2Score(self):
        self.p2Score += 1

    def writeScore(self):
        self.undo()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(0, 250)
        self.write(f"{self.p1Score} : {self.p2Score}", True,
                   'center', ('Arial', 30, 'bold'))

    def refreshScore(self):
        self.updateScore()
        self.writeScore()

    def gameOver(self):
        self.setpos(0, 0)
        self.write('GAME OVER', True, 'center', ('Arial', 15, 'bold'))
