import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard


def game():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.listen()

    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.spawn_food()
            snake.extend()
            scoreboard.score_up()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()
            # return

        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                # return


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    game()
    screen.exitonclick()
