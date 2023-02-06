from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.readHighscore()
        self.writeScore()

    def readHighscore(self):
        with open('highscore') as file:
            highscore = file.read()
            self.high_score = int(highscore)

    def updateHighscore(self):
        with open('highscore', mode='w') as file:
            file.write(str(self.high_score))

    def updateScore(self):
        self.score += 1

    def writeScore(self):
        self.undo()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.text = 'Score : ' + str(self.score) + \
            ' Highscore : ' + str(self.high_score)
        self.write(self.text, True, 'center', ('Arial', 15, 'bold'))

    def refreshScore(self):
        self.updateScore()
        self.writeScore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updateHighscore()
        self.writeScore()
    # def gameOver(self):
        # self.setpos(0, 0)
        # self.write('GAME OVER', True, 'center', ('Arial', 15, 'bold'))
