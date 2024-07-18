import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.choices = ["Rock", "Paper", "Scissors"]
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=('normal', 20))
        self.label.pack(pady=20)

        self.rock_button = tk.Button(self.root, text="Rock", font=('normal', 20), command=lambda: self.play("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_button = tk.Button(self.root, text="Paper", font=('normal', 20), command=lambda: self.play("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_button = tk.Button(self.root, text="Scissors", font=('normal', 20), command=lambda: self.play("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

