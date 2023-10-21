from turtle import Turtle, mode, width

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = self._load_highscore()
        self.color("white")
        self.up()
        self.goto(x=0,y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self._save_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def _load_highscore(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def _save_highscore(self, highscore):
        with open("data.txt", mode="w") as file:
            file.write(str(highscore))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_scoreboard()
