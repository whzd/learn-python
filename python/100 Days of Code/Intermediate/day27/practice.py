import tkinter
from tkinter import font
from tkinter.constants import X

window = tkinter.Tk()
window.title("Practice TK")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
lbl_test = tkinter.Label(text="Testing a label.", font=("Arial", 24, font.ITALIC))
lbl_test.grid(row=0, column=0)

def button_clicked():
    if input.get() != "":
        lbl_test.config(text=input.get())
    else:
        lbl_test.config(text="Button Got Clicked")

# Button1
btn = tkinter.Button(text="Click Me", command=button_clicked)
btn.grid(row=1, column=1)

# Button 2
btn2 = tkinter.Button(text="Don't Click Me")
btn2.grid(row=0, column=2)

# Entry
input = tkinter.Entry()
input.grid(row=2, column=3)

window.mainloop()
