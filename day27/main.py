from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
# Label
my_label = Label(text="I am a Label", font=("Arial", 14, "normal"))
my_label.grid(column=0, row=0)

# Entry

input_box = Entry(width=10)
input_box.insert(END, string="Placeholder")
input_box.grid(column=3, row=2)


# Button
def button_clicked():
    my_label.config(text=f"Button Clicked with Text: {input_box.get()}")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

window.mainloop()
