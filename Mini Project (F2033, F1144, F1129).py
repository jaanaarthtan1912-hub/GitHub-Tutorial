print("Name: KIRTESSHWARA RAO A/L PRAKASH, JAANAARTHTAN A/L GANESAN, YALINIYAN A/L BHUVANESWARAN ")
print("Registration Number: 25DDT22F1144, 25DDT22F2033, 25DDT21F1129 ")
print("Class: DDT4SAD1")
print("Mini Project 1\n")

import tkinter as tk
from tkinter import messagebox
import random

# Load questions from text file
def load_questions_from_file(filename):
    questions = {"beginner": [], "intermediate": [], "advanced": []}
    with open(filename, 'r') as file:
        level = None
        for line in file:
            line = line.strip()
            if line.startswith("level:"):
                level = line.split(":")[1]
            elif line and level in questions:
                parts = line.split("|")
                if len(parts) == 6:  # question, option1, option2, option3, option4, answer
                    questions[level].append(parts)
    return questions

# Display game information
def show_information():
    info_text = (
        "Instructions:\n"
        "1. Click 'Start Game' to begin.\n"
        "2. Select the correct option for each question.\n"
        "3. Your score will be displayed at the end.\n"
        "4. Click 'Exit' to quit the game."
    )
    messagebox.showinfo("Game Info", info_text)

# Display quiz questions for the selected level
def start_game(level):
    quiz_questions = questions.get(level, [])
    if not quiz_questions:
        messagebox.showerror("Error", "No questions available.")
        return

    random.shuffle(quiz_questions)  # Shuffle questions
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Python Quiz Game - {level.capitalize()}")
    quiz_window.configure(bg="#f0f8ff")  # Light background for quiz window

    # Set the timer based on level
    if level == 'beginner':
        time_limit = 3 * 60  # 3 minutes
    elif level == 'intermediate':
        time_limit = 5 * 60  # 5 minutes
    else:
        time_limit = 7 * 60  # 7 minutes

    current_question = 0
    score = 0  # Initialize score

    # Timer function
    def countdown(time_left):
        minutes = time_left // 60
        seconds = time_left % 60
        timer_label.config(text=f"Time Left: {minutes:02d}:{seconds:02d}")
        if time_left > 0:
            quiz_window.after(1000, countdown, time_left - 1)
        else:
            messagebox.showinfo("Time Up!", f"Time's up! Your score: {score}/{len(quiz_questions)}")
            quiz_window.destroy()

    # Function to display each question and update UI elements
    def show_question():
        if current_question < len(quiz_questions):
            question, *options, answer = quiz_questions[current_question]
            lbl_question.config(text=question)
            for i, option in enumerate(options):
                radio_buttons[i].config(text=option, value=option)
            selected_option.set("")
        else:
            messagebox.showinfo("Quiz Complete", f"You have finished the quiz! Your score: {score}/{len(quiz_questions)}")
            quiz_window.destroy()

    # Handle answer submission
    def submit_answer():
        nonlocal current_question, score
        selected_answer = selected_option.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        # Check if the selected answer is correct
        if selected_answer == quiz_questions[current_question][-1]:  
            score += 1  
        current_question += 1
        show_question()

    # Timer label
    timer_label = tk.Label(quiz_window, text="", font=("Arial", 14), fg="red", bg="#f0f8ff")
    timer_label.pack(pady=10)
    countdown(time_limit)  # Start the countdown timer

    lbl_question = tk.Label(quiz_window, text="", font=("Arial", 14), bg="#f0f8ff", wraplength=300)
    lbl_question.pack(pady=20)

    selected_option = tk.StringVar()
    radio_buttons = [tk.Radiobutton(quiz_window, variable=selected_option, font=("Arial", 12), bg="#f0f8ff") for _ in range(4)]
    for rb in radio_buttons:
        rb.pack(anchor="w", padx=20)

    tk.Button(quiz_window, text="Submit", command=submit_answer, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)
    show_question()

# Choose the quiz level
def choose_level():
    level_window = tk.Toplevel(root)
    level_window.title("Choose Difficulty Level")
    level_window.configure(bg="#ffebcd")
    tk.Label(level_window, text="Select the difficulty level:", font=("Arial", 14, "bold"), bg="#ffebcd").pack(pady=10)
    
    for level in questions.keys():
        tk.Button(
            level_window, text=level.capitalize(),
            command=lambda l=level: start_game(l),
            font=("Arial", 12, "bold"), bg="#ff7f50", fg="white", width=15
        ).pack(pady=5)

# Exit the application
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()

# Load questions from file
questions = load_questions_from_file("C:/Users/User/Downloads/questions.txt")

# Create main application window
root = tk.Tk()
root.title("Mini Project")
root.geometry("500x300")
root.configure(bg="#1e90ff")  # Set a calming blue background for the main window

# Title label
title_label = tk.Label(root, text="Python Quiz Game", font=("Arial", 24, "bold"), bg="#1e90ff", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Create main menu buttons
tk.Button(root, text="Information", width=20, command=show_information, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").grid(row=1, column=0, padx=10, pady=30)
tk.Button(root, text="Game", width=20, command=choose_level, font=("Arial", 12, "bold"), bg="#FFDE21", fg="white").grid(row=1, column=1, padx=10, pady=30)
tk.Button(root, text="Exit", width=20, command=exit_app, font=("Arial", 12, "bold"), bg="#f44336", fg="white").grid(row=1, column=2, padx=10, pady=30)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()