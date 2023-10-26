import tkinter as tk

# Function to display weather data (sample data)
def display_weather_data():
    location = location_entry.get()
    temperature = "72°F"  # Sample temperature
    conditions = "Sunny"  # Sample weather conditions
    weather_data_label.config(text=f"Weather in {location}: {temperature}, {conditions}")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x200")

# Create a label for location
location_label = tk.Label(root, text="Enter location:", font=("Arial", 14))
location_label.pack(pady=10)

# Create an entry widget for location
location_entry = tk.Entry(root, font=("Arial", 14))
location_entry.pack()

# Create a button to display weather data
get_weather_button = tk.Button(root, text="Get Weather", command=display_weather_data, font=("Arial", 14))
get_weather_button.pack(pady=10)

# Create a label for weather data
weather_data_label = tk.Label(root, text="", font=("Arial", 14))
weather_data_label.pack()

# Start the GUI application
root.mainloop()
