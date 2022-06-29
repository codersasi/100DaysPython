import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIMER = 3
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    flip_timer = window.after(FLIP_TIMER * 1000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")


def unknown_word():
    next_card()


def known_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_TIMER * 1000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=unknown_word)
cross_button.config(padx=50, pady=0)
cross_button.grid(row=1, column=0, columnspan=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=known_word)
check_button.config(padx=50, pady=0)
check_button.grid(row=1, column=1, columnspan=1)
next_card()
window.mainloop()
