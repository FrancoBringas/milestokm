from tkinter import *


def button_clicked():
    print(" y got clicked")
    result = int(input.get()) * 1.6
    my_result1.config(text=result)


window = Tk()
window.title("mile to KM converter")
window.minsize(width=400, height=200)

# Label
my_label = Label(text="miles", font=("Arial", 24, "bold"))
my_label.grid(column=4, row=0)

my_result = Label(text="is equal to", font=("Arial", 24, "bold"))
my_result.grid(column=1, row=2)

my_result1 = Label(text="0", font=("Arial", 24, "bold"))
my_result1.grid(column=2, row=2)

my_result2 = Label(text="KM", font=("Arial", 24, "bold"))
my_result2.grid(column=3, row=2)
# Button
new_button = Button(text="Calculate", command=button_clicked)
new_button.grid(column=3, row=3)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=0)


window.mainloop()
