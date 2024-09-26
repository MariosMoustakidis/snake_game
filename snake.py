from turtle import Turtle
import turtle

STARTING_POSITIONS = ((0,0), (-20,0), (-40,0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    turtle.colormode(255)
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position, "white")

    def add_segment(self, position, color):
        s = Turtle(shape="square")
        s.penup()
        s.color(color)
        s.goto(position)
        self.snake.append(s)

    def extend(self, color):
        self.add_segment(self.snake[-1].position(), color)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)


    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
