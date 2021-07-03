import art
import random
import game_data
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def getNewOption(prevOption):
    new_option = random.choice(game_data.data)
    while new_option == prevOption:
        new_option = random.choice(game_data.data)
    return new_option


def evaluatechoice(choice, optionA, optionB):
    if (optionB["follower_count"] > optionA["follower_count"]):
        return choice == "higher"
    else:
        return choice == "lower"


def showOptions(optionA, optionB):
    print(f"A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}.")
    print(f"Follower count: {optionA['follower_count']}M")
    print(art.vs)
    print(f"B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}.")

def game():
    print(art.logo)
    print("Welcome to the Higher vs. Lower game !")
    print("You have to guess if B has a higher or lower Intagram follower count than A.")
    print()
    score = 0
    optionA = random.choice(game_data.data)
    optionB = getNewOption(optionA)
    while True:
        showOptions(optionA, optionB)
        player = input("Type \"higher\" or \"lower\": ")
        while player != "higher" and player != "lower":
            print(f"\n{player} is not a valid option!")
            player = input("\nType \"higher\" or \"lower\": ")
        if evaluatechoice(player, optionA, optionB):
            score += 1
            optionA = optionB
            optionB = getNewOption(optionA)
            clear()
            print(art.logo)
            print(f"Right! Current score: {score}.")
            print()
        else:
            clear()
            print(art.logo)
            print(f"Wrong! Your score was: {score}.")
            print()
            showOptions(optionA, optionB)
            print(f"Follower count: {optionB['follower_count']}M")
            return




if __name__ == "__main__":
    game()