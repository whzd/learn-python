from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry Input
input = Entry(width=8)
input.grid(row=0, column=1)

# Label Miles
lbl_miles = Label(text="Miles")
lbl_miles.grid(row=0, column=2)

# Label equals
lbl_equals = Label(text="is equal to")
lbl_equals.grid(row=1, column=0)

# Label Km
lbl_km = Label(text="Km")
lbl_km.grid(row=1, column=2)

# Label Result
lbl_result = Label(text="0")
lbl_result.grid(row=1, column=1)

# Function
def calculate():
    if input.get() != "":
        lbl_result.config(text=(float(input.get())*1.60934))

# Button Calculate
btn_calculate = Button(text="Calculate", width=7, command=calculate)
btn_calculate.grid(row=2, column=1)

# Main loop
window.mainloop()
