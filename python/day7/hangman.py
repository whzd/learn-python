import random
import hangman_art
import hangman_words

from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

lifes = 6
game_over = False
word = random.choice(hangman_words.word_list)
display = ["_"]*len(word)
guessed_letters = []

print(hangman_art.logo)
print()
print(f"Your word is: {' '.join(display)}\n")


while not game_over:
    guess = input("Guess a letter: ").lower()
    clear()
    print(hangman_art.logo)
    print()
    if guess in guessed_letters:
        print(f"You already tried the letter '{guess}'!\n")
        print(f"Your word is: {' '.join(display)}\n")
    else:
        guessed_letters.append(guess)

        if guess not in word:
            print(f"The letter '{guess}' is not on the word. You lost a life!\n")
            lifes -= 1
        else:
            print("Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess

        print(f"Your word is: {' '.join(display)}\n")
        print(hangman_art.stages[lifes])

        if lifes == 0:
            game_over = True
            print(f"You loose!\nYour word was \"{word}\"")

        elif not "_" in display:
            game_over = True
            print("You Win!")
