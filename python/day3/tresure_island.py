print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Play by the rules or DIE!")
decision1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if decision1 == "right":
    print("You fell into a hole. Game Over.")
elif decision1 == "left":
    decision2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if decision2 == "swim":
        print("You were attacked by a shoal of trouts. Game Over.")
    elif decision2 == "wait":
        decision3 = input("You arrive at the island. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?\n").lower()
        if decision3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif decision3 == "red":
            print("You enter a a room of fire. Game Over.")
        elif decision3 == "yellow":
            print("You enter the tresure room. Congratulations! You Win.")
        else:
            print("That is not an option! You were struck by lighting and died. Game Over.")
    else:
        print("That is not an option! You were struck by lighting and died. Game Over.")
else:
    print("That is not an option! You were struck by lighting and died. Game Over.")
