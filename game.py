# I acknowledge the use of ChatGPT (OpenAI, GPT-5.1) to co-create this file.

import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    print("----------------------------------")

    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in options:
            print("Invalid choice! Please try again.\n")
            continue

        computer_choice = random.choice(options)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!\n")
        else:
            print("You lose!\n")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play()
