from os import stat
import turtle
import pandas


FONT = ("Courier", 12, "normal")


def _place_text(x, y, text):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x,y)
    t.write(arg=text, align="left", font=FONT)


def _export_missed_states(states_data, guessed_states):
    index_to_drop = [states_data.index[states_data.state == state].tolist()[0] for state in guessed_states]
    missed_data = states_data.drop(index_to_drop)
    missed_dict = {"Missied States": missed_data.state}
    pandas.DataFrame(missed_dict).to_csv("missed_states.csv")


def game():
    states_data = pandas.read_csv("50_states.csv")
    guessed_states = []
    while len(guessed_states) < 50:
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a state in the map.").title()
        if answer == "Exit":
            _export_missed_states(states_data, guessed_states)
            return
        elif answer in states_data.state.values and answer not in guessed_states:
            state = states_data[states_data.state == answer]
            _place_text(int(state["x"]), int(state["y"]), answer)
            guessed_states.append(answer)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Name The States")
    image = "./blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    game()
