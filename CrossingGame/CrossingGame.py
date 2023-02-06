import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
carmanager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.onkey(player.move, 'Up')
game_is_on = True
scoreboard.writeScore()
while game_is_on:
    if player.checkWin():
        carmanager.increaseLevel()
        scoreboard.refreshScore()
    elif player.checkLose(carmanager.cars):
        scoreboard.gameOver()
        game_is_on = False
    else:
        carmanager.addCars()
        carmanager.moveCars()
    time.sleep(0.1)
    screen.update()
