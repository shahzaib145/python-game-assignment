# I acknowledge the use of ChatGPT (OpenAI, GPT-5.1) to co-create this file.

import random
import tkinter as tk
from tkinter import messagebox

def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo(
        "Result",
        f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    )

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x300")

label = tk.Label(root, text="Choose an option:", font=("Arial", 14))
label.pack(pady=20)

btn_rock = tk.Button(root, text="Rock", width=15, command=lambda: play("rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=15, command=lambda: play("paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors"))
btn_scissors.pack(pady=5)

root.mainloop()
