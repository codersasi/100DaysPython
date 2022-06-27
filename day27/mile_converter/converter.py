from tkinter import *

FONT = ("Ariel", 18, "normal")
window = Tk()
window.config(bg="white")
# window.minsize(width=200, height=150)
window.title("Miles to Km Converter")
window.config(padx=25, pady=25)

# Entry
miles_input = Entry(width=10)
miles_input.config(bg="white")
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)
# Miles Label
miles_label = Label(text="Miles", font=FONT)
miles_label.config(bg="white")
miles_label.grid(column=2, row=0)
# Equals Label
equals_label = Label(text="is equal to", font=FONT)
equals_label.config(bg="white")
equals_label.grid(column=0, row=1)
# Km Converted Label
km_converted = Label(text="0", font=FONT)
km_converted.config(bg="white")
km_converted.grid(column=1, row=1)
# Label
km_label = Label(text="Km", font=FONT)
km_label.config(bg="white")
km_label.config(padx=2, pady=2)
km_label.grid(column=2, row=1)


# Button
def calculate():
    miles = float(miles_input.get())
    kms = miles * 1.609
    km_converted.config(text=f"{kms}")


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.config(bg="white")
calculate_button.grid(column=1, row=2)

window.mainloop()
