import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list3 = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    passwd_entry.delete(0, END)
    passwd_entry.insert(0, password)
    pyperclip.copy(text=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = passwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Website/Password cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered\n"
                                               f"Email: {username}\n"
                                               f"Password: {password}\n"
                                               f"Is it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                username_entry.insert(0, "sasi.ch85@gmail.com")
                passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
passwd_label = Label(text="Password:")
passwd_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.insert(0, "sasi.ch85@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)
passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
