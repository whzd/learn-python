import art
import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit(hand):
    newCard = random.choice(cards)
    if newCard == 11 and sum(hand) + newCard > 21:
        newCard = 1
    elif 11 in hand and sum(hand) + newCard > 21:
        hand[hand.index(11)] = 1
    hand.append(newCard)


def freshGame(player, computer):
    for _ in range(2):
        hit(player)
        hit(computer)


def checkBust(hand):
    if sum(hand) > 21:
        return True
    else:
        return False
    

def winningCondition(player, computer):
    if sum(player) == sum(computer):
        return "\nDRAW"
    if sum(player) > sum(computer):
        return "\nYOU WIN!"
    else:
        return "\nYOU LOSE!"
    

def showUI(player, computer, actionMsg, msg):
    clear()
    print(art.logo)
    if actionMsg:
        print(actionMsg)
    if msg:
        print(f"Your cards: {player}\nCurrent Score: {sum(player)}")
        print(f"Computer cards: {computer}\nCurrent Score: {sum(computer)}")
        print(msg)
    else:
        print(f"Your cards: {player}\nCurrent Score: {sum(player)}")
        print(f"Computer cards: [{computer[0]}, *]\nCurrent Score: {computer[0]}")


def play():
    player = []
    computer = []
    freshGame(player, computer)
    showUI(player, computer, None, None)
    if sum(player) == 21:
        showUI(player, computer, "BLACKJACK!\n", "\nYOU WIN")
        return 
    while True:
        playerchoice = input("\nDo you want to \"hit\" or \"stay\"?\n")
        if playerchoice == "hit":
            hit(player)
            if checkBust(player):
                showUI(player, computer, "Player hit.\n", "\nYOU LOSE: Player bust!")
                return 
            showUI(player, computer, "Player hit.\n", None)
        elif playerchoice == "stay":
            while sum(computer) < 17:
                hit(computer)
            if checkBust(computer):
                showUI(player, computer, "Player stay.\n", "\nYOU WIN: Computer bust!")
                return 
            showUI(player, computer, "Player stay.\n", winningCondition(player, computer))
            return
        else:
            print("Invalid input.")
    
if __name__ == "__main__":
    clear()
    print(art.logo)
    print("Welcome to the casino blackjack!\n")
    playing = False
    choice = input("Would you like to play? Type \"y\" or \"n\"\n")
    if choice == "y":
        playing = True
    while playing:
        play()
        choice = input("\nWould you like to play again? Type \"y\" or \"n\"\n")
        if choice == "n":
            playing = False
