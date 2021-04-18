import art
import string

alphabet = list(string.ascii_lowercase)
symbols = list(string.punctuation)

from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def caesar(direction, text, shift):
    newText = ""
    overflow = -len(alphabet)
    if shift >= len(alphabet):
        shift = shift % len(alphabet)
    if direction == "decode":
        shift *= -1
        overflow *= -1
    for letter in text:
        if letter.isalpha():
            position = alphabet.index(letter)
            if position + shift >= len(alphabet) or position + shift < 0:
                newText += alphabet[position + shift + overflow]
            else:
                newText += alphabet[position + shift]
        else:
            newText += letter
    return newText

stop = False
while not stop:
    clear()
    print(art.logo)
    direction = input("Type \"encode\" to encrypt, type \"decode\" to decrypt:\n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f"The {direction}d text is \"{caesar(direction,text, shift)}\"")
    else:
        print("That is not an option.")
    stopping = input("Type \"yes\" if you want to go again. Otherwise type \"no\".\n")
    if stopping == "no":
        stop = True
        print("Goodbye")