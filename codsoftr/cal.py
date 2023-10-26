import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = result_display.get()
    result_display.delete(0, tk.END)
    result_display.insert(0, current + str(number))

# Function to clear the display
def clear_display():
    result_display.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        expression = result_display.get()
        result = eval(expression)
        result_display.delete(0, tk.END)
        result_display.insert(0, result)
    except:
        result_display.delete(0, tk.END)
        result_display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")  # Set the dimensions (width x height)

# Set a background color for the main window
root.configure(bg="#0099cc")

# Create an entry widget for displaying the result
result_display = tk.Entry(root, width=20, font=("Arial", 20))
result_display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Create buttons for digits and operations with custom colors
buttons = [
    ('7', 1, 0, "#0099cc"), ('8', 1, 1, "#0099cc"), ('9', 1, 2, "#0099cc"), ('/', 1, 3, "#ff6600"),
    ('4', 2, 0, "#0099cc"), ('5', 2, 1, "#0099cc"), ('6', 2, 2, "#0099cc"), ('*', 2, 3, "#ff6600"),
    ('1', 3, 0, "#0099cc"), ('2', 3, 1, "#0099cc"), ('3', 3, 2, "#0099cc"), ('-', 3, 3, "#ff6600"),
    ('0', 4, 0, "#0099cc"), ('C', 4, 1, "#ff6600"), ('=', 4, 2, "#ff6600"), ('+', 4, 3, "#ff6600")
]

for (text, row, col, color) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=10, height=3, bg=color, command=clear_display)
    elif text == '=':
        button = tk.Button(root, text=text, width=10, height=3, bg=color, command=evaluate)
    else:
        button = tk.Button(root, text=text, width=10, height=3, bg=color, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=10, pady=10)

# Start the GUI application
root.mainloop()
