import time
from turtle import Screen
from snake import Snake


def game():
    snake = Snake()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.listen()

    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    game()
    screen.exitonclick()