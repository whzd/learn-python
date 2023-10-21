import art
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    print(art.icon)
    print("Welcome to the Coffee Machine!")
    while True:
        choice = input(f"\nWhat coffee do you want? ({menu.get_items()[:-1]}): ")
        if choice == "off":
            return
        if choice == "report":
            print("\nReport")
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    start()