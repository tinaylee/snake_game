from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=FONT)