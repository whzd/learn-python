import art
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def find_highest_bidder(bidding_record):
    highest = -1
    highest_name = ""
    for key in auction:
        if auction[key] > highest:
            highest_name = key
            highest = auction[key]
    print(f"The winner is {highest_name} with a bid of ${highest}.")

print(art.logo)
print("Welcome to the secret auction program.")
auction = {}
stop = False
while not stop:
    name = input("Enter bidder's name: ")
    bid = int(input("Enter bidder's bid: $"))
    auction[name] = bid
    stopping = input("Are there any other bidders? Type \"yes\" or \"no\".\n")
    if stopping == "no":
        stop = True
    clear()

find_highest_bidder(auction)

