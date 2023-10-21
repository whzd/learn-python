from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(x_pos, y_pos)
        self.resizemode("user")
        self.turtlesize(stretch_len=5)
        self.speed("fastest")

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
