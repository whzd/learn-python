from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard


def game():
    r_paddle = Paddle(350,0)
    l_paddle = Paddle(-350,0)
    ball = Ball()
    r_scoreboard = Scoreboard(100,200)
    l_scoreboard = Scoreboard(-100,200)

    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")
    screen.listen()

    while True:
        screen.update()
        ball.move()

        # wall bounce
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        # r_paddle hit
        if (ball.xcor() > 320 and ball.distance(r_paddle) < 55) or (ball.xcor() < -320 and ball.distance(l_paddle) < 55):
            ball.hit()

        # l_paddle score
        if ball.xcor() > 380:
            l_scoreboard.score_up()
            ball.reset()

        # r_paddle score
        if ball.xcor() < -380:
            r_scoreboard.score_up()
            ball.reset()


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.tracer(0)
    game()
    screen.exitonclick()
