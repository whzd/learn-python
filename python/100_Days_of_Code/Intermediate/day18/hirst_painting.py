import turtle
import colorgram
import random
from turtle import Turtle


def _get_color_list():
    image_colors = colorgram.extract('hirst-severed-spots.jpg', 30)
    colors = []
    for color in image_colors:
        colors.append(tuple(color.rgb))
    return colors[3:]


def create_dot(turtle, color_list):
    selected_color = random.choice(color_list)
    turtle.pencolor(selected_color)
    turtle.dot(20)


def create_painting(turtle, color_list):
    for x in range (-350, 350, 70):
        for y in range(-350, 350, 70):
            turtle.up()
            turtle.goto(y,x)
            turtle.down()
            create_dot(turtle, color_list)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.colormode(255)
    turtle = Turtle()
    turtle.speed(0)
    color_list = _get_color_list()
    create_painting(turtle, color_list)
    screen.exitonclick()