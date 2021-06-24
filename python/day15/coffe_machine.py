import art
import data


def checkStock(coffeeType, stock):
    for ingredient, quantity in data.menu[coffeeType]["ingredients"].items():
        if quantity > stock[ingredient]:
            print(f"Sorry not enough {ingredient} in stock.\nRequires {quantity} has {stock[ingredient]}.")
            return False
    return True


def work(coffeeType, stock):
    for ingredient, quantity in data.menu[coffeeType]["ingredients"].items():
        stock[ingredient] -= quantity


def report(stock, profit):
    print("\nStock report.")
    for ingredient, quantity in stock.items():
        if ingredient == "coffee":
            print(f"{ingredient.capitalize()}: {quantity}g")
        print(f"{ingredient.capitalize()}: {quantity}ml")
    print(f"Money: ${profit}")


def collectCoins():
    print("\nPlease insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

def start():
    print(art.icon)
    print("Welcome to the coffee machine!")
    profit = 0
    while True:
        choice = input("\nWhat coffee do you want ? (espresso/latte/cappuccino)\n")
        if choice == "off":
            return
        elif choice == "report":
            report(data.resources, profit)
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            if checkStock(choice, data.resources):
                price = data.menu[choice]["cost"]
                deposit = collectCoins()
                if deposit >= price:
                    if deposit > price:
                        print(f"Here is ${deposit-price} in change.")
                    work(choice, data.resources)
                    print(f"Here is your {choice} ☕️ Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"\n{choice} is an invalid option!")


if __name__ == "__main__":
    start()