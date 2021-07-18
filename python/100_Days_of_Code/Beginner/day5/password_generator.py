import random
import string
letters = string.ascii_letters
numbers = string.digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers
password = ""
for i in range(0, password_length):
    if i < nr_letters:
        password += random.choice(letters)
    elif i < nr_letters + nr_symbols:
        password += random.choice(symbols)
    else:
        password += random.choice(numbers)

print(f"Here is your password: {''.join(random.sample(password,password_length))}")