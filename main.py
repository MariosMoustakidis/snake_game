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

paused = False
game_is_on = True
while game_is_on:
    if not paused:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            snake.extend(food.get_color())
            food.refresh()
            score.update()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()
            time.sleep(0.5)


        # Detect collision with tail.
        for segment in snake.snake:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
                time.sleep(0.5)



