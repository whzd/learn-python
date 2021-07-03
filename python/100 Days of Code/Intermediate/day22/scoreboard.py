from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_pos,y_pos)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()

