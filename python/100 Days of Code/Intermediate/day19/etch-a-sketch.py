from turtle import Turtle, Screen, clear


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def turn_clockwise():
    turtle.right(10)


def turn_counter_clockwise():
    turtle.left(10)


def clear_screen():
    turtle.clear()
    turtle.up()
    turtle.home()
    turtle.down()


def game(screen):
    screen.onkey(key="Up", fun=move_forward)
    screen.onkey(key="Down", fun=move_backwards)
    screen.onkey(key="Right", fun=turn_clockwise)
    screen.onkey(key="Left", fun=turn_counter_clockwise)
    screen.onkey(key="c", fun=clear_screen)


if __name__ == "__main__":
    screen = Screen()
    screen.listen()
    turtle = Turtle()
    turtle.speed(9)
    game(screen)
    screen.exitonclick()

