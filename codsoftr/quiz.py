import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Earth"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
        "correct_answer": "Blue Whale"
    }
]

# Initialize variables
question_index = 0
score = 0

# Function to display the next question
def next_question():
    global question_index, score
    if question_index < len(quiz_data):
        question_label.config(text=quiz_data[question_index]["question"])
        for i in range(4):
            option_buttons[i].config(text=quiz_data[question_index]["options"][i], state="normal")
    else:
        messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(quiz_data)}")
        root.destroy()

# Function to check the selected answer
def check_answer(answer):
    global question_index, score
    correct_answer = quiz_data[question_index]["correct_answer"]
    if answer == correct_answer:
        score += 1
    question_index += 1
    next_question()

# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x400")  # Set the dimensions (width x height)
root.configure(bg="#0099cc")  # Set background color

# Create a label for the question
question_label = tk.Label(root, text="", bg="#0099cc", fg="white", font=("Arial", 14))
question_label.pack(pady=20)

# Create buttons for answer choices
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", bg="#ff6600", fg="white", font=("Arial", 12), width=20, height=2,
                       command=lambda i=i: check_answer(quiz_data[question_index]["options"][i]), state="disabled")
    option_buttons.append(button)
    button.pack(pady=10)

# Create a button to start the quiz
start_button = tk.Button(root, text="Start Quiz", bg="#0099cc", fg="white", font=("Arial", 14), command=next_question)
start_button.pack(pady=20)

# Start the GUI application
root.mainloop()
