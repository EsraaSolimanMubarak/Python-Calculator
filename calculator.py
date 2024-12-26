from tkinter import *

# create the app interface
root = Tk()
root.title("Advanced Calculator")
root.geometry("310x400")
root.resizable(False, False)
root.configure(bg="black")

# create the display
e = Entry(root, bd=10, width=18, font="Arial 22", bg="lightGrey", justify="right")
e.grid(row=0, column=0, columnspan=4, pady=(0, 5))

# buttons functionality
def click(num):
    e.insert(END, str(num))

def clear():
    e.delete(0, END)

def equal():
    try:
        # arithmitic inputs
        result = eval(e.get().replace("÷", "/").replace("x", "*"))
        clear()
        e.insert(END, str(result))
    except:
        clear()
        e.insert(END, "Error")

# create buttons
button_texts = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(button_texts):
    for j, text in enumerate(row):
        if text == "=":
            btn = Button(root, text=text, font="Arial 19 bold", bg="khaki", bd=5, width=4, height=2, command=equal)
        elif text == "C":
            btn = Button(root, text=text, font="Arial 19 bold", bg="crimson", bd=5, width=4, height=2, command=clear)
        else:
            btn = Button(root, text=text, font="Arial 19 bold", bg="grey", bd=5, width=4, height=2, command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j, padx=0, pady=0)  # No padding between buttons

root.mainloop()