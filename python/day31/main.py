import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_TEXT_COLOR = "#FFF"
CARD_FRONT_TEXT_COLOR = "#000"
NEW_LANGUAGE = "French"
BASE_LANGUAGE = "English"
random_word = None
timer = None
data = None

# ---------------------------- Load data ------------------------- #
def load_data():
    global data
    try:
        data = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")

# ------------------------ Save the progress --------------------- #
def save_progress():
    global data
    pandas.DataFrame(data).to_csv("./data/words_to_learn.csv", index=False)

def check_press():
    global data
    global random_word
    if not random_word:
        get_new_card()
    else:
        data.remove(random_word)
        save_progress()
        get_new_card()


# ------------------------- Flip the Card ------------------------ #
def flip_card():
    card.itemconfig(card_img, image=img_card_back)
    card.itemconfig(card_lang, text=BASE_LANGUAGE, fill=CARD_BACK_TEXT_COLOR)
    card.itemconfig(card_text, text=random_word[BASE_LANGUAGE], fill=CARD_BACK_TEXT_COLOR)
    window.after_cancel(timer)

# ------------------------- New Flash Card ----------------------- #
def get_new_card():
    global random_word
    global timer
    random_word = random.choice(data)
    card.itemconfig(card_img, image=img_card_front)
    card.itemconfig(card_lang, text=NEW_LANGUAGE, fill=CARD_FRONT_TEXT_COLOR)
    card.itemconfig(card_text, text=random_word[NEW_LANGUAGE], fill=CARD_FRONT_TEXT_COLOR)
    timer = window.after(3000, flip_card)

# ------------------------------ UI ------------------------------ #
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# FlashCard
card = Canvas(width=800, height=526, highlightbackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, bd=0)
img_card_back = PhotoImage(file="./images/card_back.png")
img_card_front = PhotoImage(file="./images/card_front.png")
card_img = card.create_image(400, 263)
card_lang = card.create_text(400, 150, text=f"Flash Card for {NEW_LANGUAGE}-{BASE_LANGUAGE}", font=("Ariel", 40, "italic"))
card_text = card.create_text(400, 263, text="Press ☑ to Start.", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

# Check Button
img_check = PhotoImage(file="./images/right.png")
btn_check = Button(image=img_check, highlightbackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, bd=0, activebackground=BACKGROUND_COLOR, command=check_press)
btn_check.grid(row=1, column=1)

# Cross Button
img_cross = PhotoImage(file="./images/wrong.png")
btn_cross = Button(image=img_cross, highlightbackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, bd=0, activebackground=BACKGROUND_COLOR, command=get_new_card)
btn_cross.grid(row=1, column=0)

load_data()
window.mainloop()
