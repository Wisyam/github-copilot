import random
import tkinter as tk
from tkinter import font as tkFont


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")
        
        self.player_score = 0
        self.computer_score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the GUI components."""
        # Title
        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=title_font,
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=15)
        
        # Instructions
        instr_label = tk.Label(
            self.root,
            text="Make your choice:",
            font=("Helvetica", 11),
            bg="#f0f0f0"
        )
        instr_label.pack(pady=(10, 5))
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        for choice in ["Rock", "Paper", "Scissors"]:
            btn = tk.Button(
                button_frame,
                text=choice,
                width=10,
                font=("Helvetica", 10),
                bg="#4CAF50",
                fg="white",
                activebackground="#45a049",
                command=lambda c=choice.lower(): self.play_game(c)
            )
            btn.pack(side="left", padx=5)
        
        # Result Frame
        result_frame = tk.Frame(self.root, bg="white", relief="sunken", bd=2)
        result_frame.pack(pady=15, padx=20, fill="both", expand=True)
        
        # Computer Choice
        self.comp_label = tk.Label(
            result_frame,
            text="Computer chose: —",
            font=("Helvetica", 10),
            bg="white"
        )
        self.comp_label.pack(pady=(10, 5))
        
        # Game Result
        self.result_label = tk.Label(
            result_frame,
            text="",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="#2196F3"
        )
        self.result_label.pack(pady=5)
        
        # Score
        self.score_label = tk.Label(
            result_frame,
            text="You: 0  |  Computer: 0",
            font=("Helvetica", 11),
            bg="white",
            fg="#666"
        )
        self.score_label.pack(pady=(5, 10))
        
        # Reset Button
        reset_btn = tk.Button(
            self.root,
            text="Reset Score",
            width=12,
            font=("Helvetica", 9),
            bg="#f44336",
            fg="white",
            activebackground="#da190b",
            command=self.reset_score
        )
        reset_btn.pack(pady=5)
    
    def play_game(self, player_choice):
        """Handle game logic when player makes a choice."""
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update score
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        # Update labels
        self.comp_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
        self.result_label.config(text=result)
        self.update_score_display()
    
    def get_computer_choice(self):
        """Get a random choice for the computer."""
        return random.choice(['rock', 'paper', 'scissors'])
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round."""
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"
    
    def update_score_display(self):
        """Update the score display."""
        self.score_label.config(
            text=f"You: {self.player_score}  |  Computer: {self.computer_score}"
        )
    
    def reset_score(self):
        """Reset the game score."""
        self.player_score = 0
        self.computer_score = 0
        self.comp_label.config(text="Computer chose: —")
        self.result_label.config(text="")
        self.update_score_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()