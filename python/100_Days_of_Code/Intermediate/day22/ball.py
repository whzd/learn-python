from turtle import Turtle, speed

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x=x_pos, y=y_pos)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.speed_up()

    def speed_up(self):
        if self.x_move < 0:
            self.x_move -= 0.3
        else:
            self.x_move += 0.3

    def reset(self):
        self.hit()
        self.goto(0,0)
        self.x_move = 3

