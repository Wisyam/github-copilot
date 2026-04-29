# Rock Paper Scissors Game - GUI Edition

A simple, interactive Rock-Paper-Scissors game with a graphical user interface built using Python's Tkinter library.

## Features

- **Interactive GUI** — User-friendly graphical interface
- **Real-time Feedback** — Immediate display of computer's choice and game result
- **Score Tracking** — Keeps track of player and computer scores throughout the game session
- **Reset Functionality** — Reset scores and start fresh at any time
- **Professional Design** — Clean layout with color-coded buttons and organized sections

## Requirements

- Python 3.6 or higher
- Tkinter (included with most Python installations)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd Project/github-copilot
   ```

## Running the Game

Execute the following command:

```bash
python main.py
```

A window will open with the game interface.

## How to Play

1. Click one of the three buttons: **Rock**, **Paper**, or **Scissors**
2. The computer will automatically make its choice
3. The game will display:
   - Computer's choice
   - Round result (You win! / Computer wins! / It's a tie!)
   - Updated scores
4. Continue playing as many rounds as you want
5. Click **Reset Score** to clear the score and start over
6. Close the window to exit the game

## Game Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- Identical choices result in a tie

## Code Structure

The game is organized into a single `RockPaperScissorsGUI` class with the following main methods:

- `__init__()` — Initializes the game and UI
- `setup_ui()` — Creates all GUI components
- `play_game()` — Handles game logic for each round
- `get_computer_choice()` — Generates random computer choice
- `determine_winner()` — Determines the round winner
- `update_score_display()` — Updates the score display
- `reset_score()` — Resets the game score

## GUI Components

- **Title** — Game name displayed at the top
- **Choice Buttons** — Three buttons for Rock, Paper, and Scissors
- **Result Section** — Displays computer's choice, game result, and scores
- **Reset Button** — Clears scores and resets the game state

## Customization

You can easily customize the game by modifying:

- Window size: Change `self.root.geometry("400x350")`
- Colors: Modify the color hex codes in button and label definitions
- Fonts: Adjust font names, sizes, and weights in tkFont definitions
- Button layout: Change `side="left"` to `side="top"` for vertical layout

## License

This project is open source and available for personal use.

## Troubleshooting

**Tkinter not found:**
- On Windows: Tkinter should be included with Python. Reinstall Python and ensure "tcl/tk and IDLE" is checked.
- On Linux: Install with `sudo apt-get install python3-tk`
- On macOS: Install with `brew install python-tk@3.x`

**Window doesn't appear:**
- Ensure no other windows are blocking it
- Try running in a different terminal
- Check that your display environment is properly configured
