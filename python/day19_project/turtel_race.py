import random
from turtle import Turtle, Screen

def _place_turtles(turtle_list):
    i = 0
    for turtle in turtle_list:
        turtle.goto(x=-230,y=-125+i)
        i += 50


def _race(turtle_list):
    _place_turtles(turtle_list)
    while True:
        for t in turtle_list:
            t.forward(random.randint(1,10))
            if t.pos()[0] >= 250:
                return t.color()


def _create_turtles(color_list):
    turtle_list = []
    for color in color_list:
        t = Turtle(shape="turtle")
        t.up()
        t.color(color)
        turtle_list.append(t)
    return turtle_list


def game(user_bet, color_list):
    turtle_list = _create_turtles(color_list)
    winner = _race(turtle_list)
    if user_bet == winner[0]:
        print("Congratulations! Your turtle won the race!")
    else:
        print(f"Too bad! The {winner[0]} turtle won the race.")


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=500,height=400)
    user_bet = screen.textinput(title="Place your bet!", prompt="Which color turtle will win the race?")
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    game(user_bet, color_list)
    screen.exitonclick()