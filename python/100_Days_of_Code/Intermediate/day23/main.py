import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def game():
    scoreboard = Scoreboard()
    player = Player()
    car_manager = CarManager()

    screen.onkey(player.move, "Up")
    screen.listen()

    while True:
        time.sleep(0.1)
        screen.update()

        car_manager.spawn_car()

        for car in car_manager.car_list:
            car_manager.move_car(car)
            if car.distance(player.position()) < 19:
                scoreboard.game_over()
                return


        if player.is_at_finish_line():
            scoreboard.level_up()
            car_manager.level_up()
            player.reset()

if __name__ == "__main__":
    screen = Screen()
    screen.title("Turtle Crossing")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    game()
    screen.exitonclick()


