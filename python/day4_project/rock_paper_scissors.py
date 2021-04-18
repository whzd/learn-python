rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

forms = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors game.")
player = int(input("What do you choose? Type \"0\" for Rock, \"1\" for Paper and \"2\" for Scissors.\n"))
print()
print("You:")
print(forms[player])

computer = random.randint(0,2)
print("Computer:")
print(forms[computer])

if player == 0 and computer == 0:
    print("Draw.")
elif player == 0 and computer == 1:
    print("You lose.")
elif player == 0:
    print("You won.")

if player == 1 and computer == 0:
    print("You won.")
elif player == 1 and computer == 1:
    print("Draw.")
elif player == 1:
    print("You lose.")

if player == 2 and computer == 0:
    print("You lose.")
elif player == 2 and computer == 1:
    print("You won.")
elif player == 2:
    print("Draw.")

