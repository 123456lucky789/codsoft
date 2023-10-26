import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    if password_length < 4:
        result_label.config(text="Password must be at least 4 characters long", fg="red")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(password_length))
        result_label.config(text="Generated Password:", fg="black")
        password_display.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")  # Set the dimensions (width x height)

# Set a background color for the main window
root.configure(bg="#0099cc")

# Create a label for the length of the password
length_label = tk.Label(root, text="Password Length:", bg="#0099cc", fg="white")
length_label.pack(pady=10)

# Create an entry widget for entering the length
length_entry = tk.Entry(root, width=5, font=("Arial", 14))
length_entry.pack()

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", bg="#ff6600", fg="white", command=generate_password)
generate_button.pack(pady=20)

# Create a label for the generated password
result_label = tk.Label(root, text="", bg="#0099cc", font=("Arial", 12))
result_label.pack()

# Create a label to display the generated password
password_display = tk.Label(root, text="", bg="white", font=("Arial", 16), relief="solid", width=20, height=1)
password_display.pack(pady=10)

# Start the GUI application
root.mainloop()
