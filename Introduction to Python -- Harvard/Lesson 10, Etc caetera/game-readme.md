# Python Command-Line Tic Tac Toe

Welcome to this exciting command-line implementation of the classic Tic Tac Toe game! This project brings the timeless game to life in your terminal, offering a clean interface and intuitive gameplay using Python, Pandas, and Tabulate.

## 🎮 Game Overview

Imagine Sarah and Mike sitting down for a friendly game of Tic Tac Toe. Sarah (Player X) and Mike (Player O) face off in an epic battle of wits on a 3x3 grid. The game board looks like this when they start:

```
╭───┬───┬───╮
│ A │ B │ C │
├───┼───┼───┤
│   │   │   │ 0
├───┼───┼───┤
│   │   │   │ 1
├───┼───┼───┤
│   │   │   │ 2
╰───┴───┴───╯
```

## 🎯 How to Play

1. **Making a Move**: Players take turns entering coordinates in the format `[Column][Row]`. For example:
   - To place your mark in the top-left corner, enter: `A0`
   - For the center position, enter: `B1`
   - For the bottom-right corner, enter: `C2`

2. **Game Flow**: 
   - Player 1 uses 'X'
   - Player 2 uses 'O'
   - Players alternate turns until someone wins or the game ends in a draw

Let's follow Sarah and Mike's game:

```
Sarah: "A0" (places X in top-left)
╭───┬───┬───╮
│ X │   │   │ 0
├───┼───┼───┤
│   │   │   │ 1
├───┼───┼───┤
│   │   │   │ 2
╰───┴───┴───╯

Mike: "B1" (places O in center)
╭───┬───┬───╮
│ X │   │   │ 0
├───┼───┼───┤
│   │ O │   │ 1
├───┼───┼───┤
│   │   │   │ 2
╰───┴───┴───╯
```

## 🔧 Technical Details

The game is built using three main components:

1. **Main Game Logic** (`main` function):
   - Checks for winning combinations:
     - Horizontal rows
     - Vertical columns
     - Diagonals
   - Returns "Player X won" or "Player O won" when a winner is found

2. **Player Turns** (`player1_turn` and `player2_turn` functions):
   - Handles input validation:
     - Ensures input is exactly 2 characters
     - Validates column (A, B, or C) and row (0, 1, or 2)
     - Checks if the chosen cell is empty
   - Places the player's mark ('X' or 'O') on the board
   - Displays the updated board after each move

3. **Draw Checker** (`draw` function):
   - Counts filled positions
   - Declares a draw if all 9 positions are filled
   - Allows game to continue if empty spaces remain

## 🚀 Getting Started

1. **Prerequisites**:
   ```bash
   pip install pandas tabulate pytest
   ```

2. **Running the Game**:
   ```bash
   python game.py
   ```

3. **Running the Tests**:
   ```bash
   pytest test_functions.py
   ```

## 🎲 Example Game: The Epic Diagonal Victory

Sarah and Mike's legendary game continues:

```
Sarah: "A0" → Mike: "B1" → Sarah: "C2"
Mike: "A2" → Sarah: "B2" → Mike: "C0"
Sarah: "A1"

Final Position:
╭───┬───┬───╮
│ X │   │ O │ 0
├───┼───┼───┤
│ X │ O │   │ 1
├───┼───┼───┤
│ O │ X │ X │ 2
╰───┴───┴───╯

Player X (Sarah) wins with a diagonal strategy!
```

## 🛠 Error Handling

The game includes robust error handling for various scenarios:

- Invalid input format: "Z9", "ABC", "11"
- Already occupied cells
- Out-of-bounds coordinates
- Non-alphabetic column input
- Non-numeric row input

When an error occurs, the game prompts the player to retry their move.

## 🏆 Winning Strategies

1. **Corner Control**: Start with corners (A0, C0, A2, C2) to maximize winning opportunities
2. **Center Dominance**: Controlling B1 gives access to four potential winning lines
3. **Blocking Technique**: Watch your opponent's moves and block their potential winning lines

Remember, a perfect game between two strategic players often ends in a draw - that's part of the beauty of Tic Tac Toe!

---

Have fun playing this classic game with a modern Python twist! May the best strategist win! 🎮✨
