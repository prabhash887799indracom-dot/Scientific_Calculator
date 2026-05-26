import tkinter as tk
from math import *

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Entry field
expression = ""

input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=('Arial', 20),
    bd=10,
    insertwidth=2,
    width=22,
    borderwidth=4,
    justify='right'
)

input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Function to clear screen
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate result
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Scientific Functions
def calculate(func):
    global expression
    try:
        value = eval(expression)

        if func == "sin":
            result = sin(radians(value))

        elif func == "cos":
            result = cos(radians(value))

        elif func == "tan":
            result = tan(radians(value))

        elif func == "sqrt":
            result = sqrt(value)

        elif func == "log":
            result = log10(value)

        elif func == "ln":
            result = log(value)

        elif func == "pi":
            result = pi

        elif func == "deg":
            result = degrees(value)

        elif func == "rad":
            result = radians(value)

        input_text.set(str(result))
        expression = str(result)

    except:
        input_text.set("Error")
        expression = ""

# Button Frame
btns_frame = tk.Frame(root)
btns_frame.pack()

# Button Layout
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
]

# Create Number Buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(
            btns_frame,
            text=text,
            width=8,
            height=3,
            font=('Arial', 14),
            command=equal
        ).grid(row=row, column=col)
    else:
        tk.Button(
            btns_frame,
            text=text,
            width=8,
            height=3,
            font=('Arial', 14),
            command=lambda t=text: press(t)
        ).grid(row=row, column=col)

# Scientific Buttons
scientific_buttons = [
    ('sin', 4, 0),
    ('cos', 4, 1),
    ('tan', 4, 2),
    ('π', 4, 3),
    ('√', 5, 0),
    ('log', 5, 1),
    ('ln', 5, 2),
    ('C', 5, 3),
    ('Deg', 6, 0),
    ('Rad', 6, 1),
]

# Create Scientific Buttons
for (text, row, col) in scientific_buttons:

    if text == 'C':
        cmd = clear

    elif text == 'sin':
        cmd = lambda: calculate("sin")

    elif text == 'cos':
        cmd = lambda: calculate("cos")

    elif text == 'tan':
        cmd = lambda: calculate("tan")

    elif text == 'π':
        cmd = lambda: calculate("pi")

    elif text == '√':
        cmd = lambda: calculate("sqrt")

    elif text == 'log':
        cmd = lambda: calculate("log")

    elif text == 'ln':
        cmd = lambda: calculate("ln")

    elif text == 'Deg':
        cmd = lambda: calculate("deg")

    elif text == 'Rad':
        cmd = lambda: calculate("rad")

    tk.Button(
        btns_frame,
        text=text,
        width=8,
        height=3,
        font=('Arial', 14),
        command=cmd
    ).grid(row=row, column=col)

# Run application
root.mainloop()
