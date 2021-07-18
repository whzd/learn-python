# Maze

The project of day 6 consists of the [Maze challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) from [Reeborg's World](https://reeborg.ca/index_en.html).

# Solution

    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    rights_in_row = 0
    while not at_goal():
        if rights_in_row == 3:
            if front_is_clear():
                move()
                rights_in_row = 0
            else:
                turn_left()
                rights_in_row = 0
        if right_is_clear():
            turn_right()
            move()
            rights_in_row += 1
        elif front_is_clear():
            move()
            rights_in_row = 0
        else:
            turn_left()