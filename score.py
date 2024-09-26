from turtle import Turtle
ALIGN = "center"
FONT = ('arial', 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, ALIGN, FONT)
        self.goto(-300, 270)
        self.pendown()
        self.goto(300, 270)
        self.penup()
        self.goto(0, 265)

    def update(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGN, FONT)
