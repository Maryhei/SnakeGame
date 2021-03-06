import time
from turtle import Turtle, Screen

import scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)


snake = Snake()
score = Scoreboard()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.clear()
        scoreboard.SCORE += 1
        score.score_counting()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
    for crash in snake.place[1:]:
        if snake.head.distance(crash) < 10:
            snake.reset()





screen.exitonclick()