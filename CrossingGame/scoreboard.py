from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.writeScore()

    def updateScore(self):
        self.score += 1

    def writeScore(self):
        self.undo()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.setpos(-200, 250)
        self.write(f"LEVEL : {self.score}", True,
                   'center', FONT)

    def refreshScore(self):
        self.updateScore()
        self.writeScore()

    def gameOver(self):
        self.setpos(0, 0)
        self.write('GAME OVER', True, 'center', FONT)
