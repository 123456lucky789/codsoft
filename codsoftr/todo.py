import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set background color for the main window
root.configure(bg="lightblue")

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectbackground="yellow", bg="lightyellow", selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Create an entry widget to add tasks
entry = tk.Entry(root, width=30)
entry.pack()

# Create buttons to add and delete tasks
add_button = tk.Button(root, text="Add Task", command=add_task, bg="lightgreen", activebackground="green")
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="lightcoral", activebackground="red")
add_button.pack(pady=5)
delete_button.pack()

# Start the application
root.mainloop()
