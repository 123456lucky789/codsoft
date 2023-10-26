import tkinter as tk
from tkinter import ttk

# Function to fetch weather data from an API (not implemented in this example)
def get_weather_data():
    # Replace this with actual API integration code
    pass

# Create the main window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x300")  # Set the dimensions (width x height)
root.configure(bg="#0099cc")  # Set background color

# Create a label for the city
city_label = tk.Label(root, text="City:", bg="#0099cc", fg="white", font=("Arial", 14))
city_label.pack(pady=10)

# Create an entry widget for entering the city
city_entry = tk.Entry(root, width=20, font=("Arial", 12))
city_entry.pack()

# Create a button to fetch weather data
get_weather_button = tk.Button(root, text="Get Weather", bg="#ff6600", fg="white", font=("Arial", 12), command=get_weather_data)
get_weather_button.pack(pady=20)

# Create a label to display the weather information
weather_label = tk.Label(root, text="", bg="#0099cc", fg="white", font=("Arial", 14))
weather_label.pack()

# Create a style for the labels and buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#ff6600")
style.configure("TLabel", font=("Arial", 14), background="#0099cc", foreground="white")

# Start the GUI application
root.mainloop()
