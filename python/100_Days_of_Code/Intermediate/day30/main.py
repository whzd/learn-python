import json
from os import walk
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ------------------------- FIND WEBSITE CREDENTIALS ---------------------------- #
def find_credentials():
    if input_website.get() != "":
        try:
            with open("./data.json", "r") as f:
                data = json.load(f)
                entry_data = data[input_website.get()]
        except FileNotFoundError:
            messagebox.showerror(title="File not found", message="There is no data saved yet.")
        except KeyError as e:
            messagebox.showerror(title="Website not found", message=f"There is no entry for the {e} website.")
        else:
            messagebox.showinfo(title=input_website.get(), message=f'Email: {entry_data["email"]}\nPassword: {entry_data["password"]}')
    else:
        messagebox.showerror(title="Empty area.", message="Can´t search for credentials if no website is provided.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def _create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2,4))]

    random.shuffle(password_list)

    return "".join(password_list)

def generate_password():
    input_password.delete(0, END)
    pw = _create_password()
    input_password.insert(0, pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def _clear_entries():
    input_user.delete(0, END)
    input_website.delete(0, END)
    input_password.delete(0, END)

def _entry_is_empty():
    return input_website.get() == "" or input_user.get() == "" or input_password.get() == ""

def save_to_file():
    if not _entry_is_empty():
        if messagebox.askokcancel(title="Confirm Input information", message=f"Website: {input_website.get()}\nUser: {input_user.get()}\nPassword: {input_password.get()}\n\nSave?"):
            new_data = {input_website.get() : {"email" : input_user.get(), "password" : input_password.get()}}
            try:
                with open("./data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = new_data
            else:
                data.update(new_data)
            finally:
                with open("./data.json", "w") as f:
                    json.dump(data, f, indent=2)
                _clear_entries()
                messagebox.showinfo(title="Success", message="Entry saved to file.")
    else:
        messagebox.showerror(title="Empty Fields", message="Please insert values in all the fields.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
cnv_bg_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=cnv_bg_img)
canvas.grid(row=0, column=1)

# Website
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0, sticky="E")
input_website = Entry(width=30)
input_website.focus()
input_website.grid(row=1, column=1, sticky="W")
btn_search = Button(text="Search", command=find_credentials, width=13)
btn_search.grid(row=1, column=2, sticky="W")

# Username/Email
lbl_user = Label(text="Email/Username:")
lbl_user.grid(row=2, column=0, sticky="E")
input_user = Entry(width=47)
input_user.grid(row=2, column=1, columnspan=2, sticky="W")

# Password
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0, sticky="E")
input_password = Entry(width=30)
input_password.grid(row=3, column=1, sticky="W")
btn_password = Button(text="Generate Password", command=generate_password, width=13)
btn_password.grid(row=3, column=2, sticky="W")

# Add
btn_add = Button(text="Add", command=save_to_file, width=44)
btn_add.grid(row=4, column=1, columnspan=2, sticky="W")


window.mainloop()
