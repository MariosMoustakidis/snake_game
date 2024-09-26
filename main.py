from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
        snake.extend(food.get_color())
        food.refresh()
        score.update()


    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 270 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()





screen.exitonclick()


