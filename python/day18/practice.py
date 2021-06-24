import random
from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.speed(0)

def random_paint():
    # Using calculations
    # # normal north
    # def east():
    #     if turtle.heading() > 180:
    #         turtle.right(360-turtle.heading())
    #     else:
    #         turtle.left(turtle.heading())

    # #normal south
    # def west():
    #     if turtle.heading() > 180:
    #         turtle.left(turtle.heading()-180)
    #     else:
    #         turtle.right(180-turtle.heading())

    # #normal east
    # def south():
    #     if turtle.heading() > 90:
    #         turtle.left(turtle.heading()-90)
    #     else:
    #         turtle.right(90-turtle.heading())

    # #normal west
    # def north():
    #     if turtle.heading() > 270:
    #         turtle.left(turtle.heading()-270)
    #     else:
    #         turtle.right(270-turtle.heading())

    # direction = [north, south, east, west]
    for _ in range (0,100):
        turtle.pencolor(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
        turtle.pensize(10)
        # aim = random.choice(direction)
        # aim()
        directions = [0, 90, 180, 270]
        turtle.setheading(random.choice(directions))
        turtle.forward(50)

def sherograph():
    for i in range(0,360, 5):
        turtle.setheading(i)
        turtle.pencolor(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
        turtle.circle(100)
        turtle.up()
        turtle.down()


sherograph()
screen.exitonclick()