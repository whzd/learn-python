import art
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def adition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

operations = {"+": adition, "-": subtraction, "*": multiplication, "/": division}
def calculator():
    print(art.logo)
    clean = False
    num1 = float(input("Insert a number: "))
    while not clean:
        prettyOP = " ".join(operations.keys())
        print(f"Operands: {prettyOP}")
        op = input("Choose and operand from the list: ")
        num2 = float(input("Insert another number: "))
        operation = operations[op]
        result = operation(num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        res = input("To continue type \"yes\" to start over type \"no\". To terminate type \"quit\".\n")
        if res == "quit":
            return
        elif res == "no":
            clean = True
            clear()
            calculator()
        else:
            num1 = result

calculator()