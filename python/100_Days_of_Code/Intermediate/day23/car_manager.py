from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_CAR_ON_SCREEN = 15
CAR_Y_SIZE = 20
CAR_X_SIZE = 40

class CarManager:

    def __init__(self) -> None:
        super().__init__()
        self.car_list = []
        self._first_spawn()
        self.car_speed = STARTING_MOVE_DISTANCE

    def _create_car(self):
        t = Turtle()
        t.color(random.choice(COLORS))
        t.shape("square")
        t.penup()
        t.setheading(180)
        t.resizemode("user")
        t.turtlesize(stretch_len=2)
        return t

    def _nearest_multiple(self, base, value):
        return base * round(value/base)

    def _first_spawn(self):
        while len(self.car_list) < MAX_CAR_ON_SCREEN:
            car = self._create_car()
            # prevent Y partial overlap
            y_pos = self._nearest_multiple(CAR_Y_SIZE, random.randint(-230, 230))
            # prevent X partial overlap
            x_pos = self._nearest_multiple(CAR_X_SIZE, random.randint(-230, 300))
            car.goto(x=x_pos, y=y_pos)
            self.car_list.append(car)

    def spawn_car(self):
        if len(self.car_list) < MAX_CAR_ON_SCREEN:
            car = self._create_car()
            # prevent Y partial overlap
            y_pos = self._nearest_multiple(CAR_Y_SIZE, random.randint(-230, 230))
            # prevent X partial overlap
            x_pos = self._nearest_multiple(CAR_X_SIZE, random.randint(300, 350))
            car.goto(x=x_pos, y=y_pos)
            self.car_list.append(car)

    def _despawn_car(self, car):
        car.hideturtle()
        self.car_list.remove(car)

    def move_car(self, car):
        car.forward(self.car_speed)
        if car.xcor() <= -280:
            self._despawn_car(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
