import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.bgcolor('black')
myScreen.title('Snake')
myScreen.tracer(0)

game_is_on = True
snake = Snake(3)
food = Food()
scoreboard = Scoreboard()
myScreen.listen()
myScreen.onkey(snake.moveLeft, 'a')
myScreen.onkey(snake.moveUp, 'w')
myScreen.onkey(snake.moveDown, 's')
myScreen.onkey(snake.moveRight, 'd')
while game_is_on:
    myScreen.update()
    time.sleep(0.1)
    snake.moveForward()
    if snake.body[0].distance(food) <= 15:
        food.refresh()
        snake.extend()
        scoreboard.refreshScore()

    if snake.body[0].xcor() > 290 or snake.body[0].xcor() < -290 or snake.body[0].ycor() > 290 or snake.body[0].ycor() < -290:
        print('wall')
        # game_is_on = False
        # scoreboard.gameOver()
        scoreboard.reset()
        snake.reset()

    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            # game_is_on = False
            # scoreboard.gameOver()
            scoreboard.reset()
            snake.reset()
            break

myScreen.exitonclick()
