from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Score import Score
import time
myScreen = Screen()
myScreen.bgcolor('black')
myScreen.setup(width=800, height=600)
myScreen.title('Pong')
myScreen.tracer(0)
player = Paddle()
enemy = Paddle(-350)
ball = Ball()
score = Score()
myScreen.onkey(enemy.moveForward, 'w')
myScreen.onkey(enemy.moveBack, 's')

myScreen.onkey(player.moveForward, 'Up')
myScreen.onkey(player.moveBack, 'Down')

myScreen.listen()
while True:
    if ball.xcor() <= -380:
        score.updateP2Score()
    if ball.xcor() >= 380:
        score.updateP1Score()
    enemy.update()
    player.update()
    ball.checkPaddle(enemy, player)
    ball.move()
    score.writeScore()
    myScreen.update()
    # time.sleep(0.01)
