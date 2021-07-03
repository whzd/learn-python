import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("Choose a dificulty. Type \"easy\" or \"hard\"\n")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS


def check_answer(guess, target, attempts):
    if guess == target:
        print(f"\nYou got it! The answer was {target}")
        return
    elif guess > target:
        print("Too high.")
        return attempts - 1
    else:
        print("Too low.")
        return attempts - 1


def play():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thingk in a number between 1 and 100.")
    attempts = set_difficulty()
    target = random.randint(1, 100)
    print(target)
    while attempts and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, target, attempts)
        if attempts:
            if attempts > 0:
                print("Guess again.")
            else:
                print(f"\nYou've run out of guesses, you lose. The number was {target}")
                return


if __name__ == "__main__":
    play()