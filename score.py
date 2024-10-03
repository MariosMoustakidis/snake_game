from turtle import Turtle
import random
ALIGN = "center"
FONT = ('arial', 24, "normal")
DEFEAT_MESSAGES = ["Oops you lost", "Better luck next time", "Hmm, you can do better", "Try again you got this", "Well...that's embarrassing", "I believe you can do this"]
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
        self.goto(-300, 270)
        self.pendown()
        self.goto(300, 270)
        self.penup()
        self.goto(0, 265)

    def update(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
        self.goto(0, 230)
        self.write(random.choice(DEFEAT_MESSAGES), align=ALIGN, font=('arial', 17, "normal"))




