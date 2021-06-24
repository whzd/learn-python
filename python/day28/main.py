from tkinter import *
from tkinter.font import BOLD
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    lbl_checkmark.config(text="")
    lbl_top.config(text="Timer", fg=GREEN)
    canvas.itemconfig(cnv_timer, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        lbl_top.config(text="Break", fg=RED)
        lbl_checkmark.config(text=lbl_checkmark.cget("text")+"✔")
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        lbl_top.config(text="Break", fg=PINK)
        lbl_checkmark.config(text=lbl_checkmark.cget("text")+"✔")
        count_down(SHORT_BREAK_MIN)
    else:
        lbl_top.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(minutes=0,seconds=0):
    global timer
    canvas.itemconfig(cnv_timer, text=f"{minutes:02}:{seconds:02}")
    if seconds > 0:
        timer = window.after(1000, count_down, minutes, seconds-1)
    elif seconds == 0 and minutes > 0:
        timer = window.after(1000, count_down, minutes-1, 59)
    elif seconds == 0 and minutes == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bk_image = PhotoImage(file="/Users/andrefilipe.dias/ff-learn/python/day28/tomato.png")
canvas.create_image(100, 112, image=bk_image)
cnv_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label top
lbl_top = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55))
lbl_top.grid(row=0, column=1)

# Button Start
btn_start = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, fg=BLACK, command=start_timer)
btn_start.grid(row=2, column=0)

# Button Reset
btn_reset = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, fg=BLACK, command=reset_timer)
btn_reset.grid(row=2, column=2 )

# Label Checkmarks
lbl_checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
lbl_checkmark.grid(row=3, column=1)


window.mainloop()
