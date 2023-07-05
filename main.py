from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)


def miles_to_km():
    miles = float(num_entered.get())
    km = round(miles * 1.609)
    num_in_km.config(text=f"{km}")


# Entry
num_entered = Entry(width=12)
num_entered.grid(column=1, row=1, )

# Label
# intro = Label(text="WELCOME TO MY PROGRAM", font=("Arial", 15, "bold"))
# intro.grid(column= 2, row= 0)

miles = Label(text="Miles", font=("Arial", 15))
miles.grid(column=2, row=1)

km = Label(text="Km", font=("Arial", 15))
km.grid(column=2, row=2)

equals = Label(text="is equals to", font=("Arial", 15))
equals.grid(column=0, row=2)

num_in_km = Label(text="0", font=("Arial", 15))
num_in_km.grid(column=1, row=2)

# Button
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=3)

window.mainloop()
