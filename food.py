from turtle import Turtle
import turtle
import random

class Food(Turtle):
    turtle.colormode(255)
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.set_color()
        self.my_color = (0, 0 ,0)
        self.refresh()


    def refresh(self):
        grid_size = 20
        random_x = random.randint(-280 // grid_size, 280 // grid_size) * grid_size
        random_y = random.randint(-280 // grid_size, 260 // grid_size) * grid_size
        self.goto(random_x, random_y)
        self.set_color()

    def set_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        self.save_color(random_color)
        self.color(random_color)

    def save_color(self, color):
        self.my_color = color

    def get_color(self):
        return self.my_color

