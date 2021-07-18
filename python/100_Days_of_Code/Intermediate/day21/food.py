import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        #TODO: only spawn food in the path of the snake (aka, the random coords must be multiple of 20)
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x=x, y=y)

