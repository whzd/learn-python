from turtle import Turtle


class Snake:

    def __init__(self) -> None:
        self.snake = self._create_snake()

    def _create_snake(self):
        snake = []
        for i in range(3):
            t = Turtle(shape="square")
            t.up()
            t.color("white")
            t.goto(x=(i*-20),y=0)
            snake.append(t)
        return snake

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)