# Four-in-a-Row (Connect Four)

A Python implementation of the classic Connect Four game with an intelligent AI opponent.

## 🎮 Game Overview

Four-in-a-Row is a strategy game where players take turns dropping colored discs into a vertical grid. The objective is to connect four of your pieces in a row - horizontally, vertically, or diagonally - before your opponent does.

**Player Symbols:**
- Player: `o` (blue circles)
- AI: `x` (red crosses)

## ✨ Features

- **Intelligent AI Opponent**:  AI that uses strategic decision-making
- **Scoring System**: Points awarded for connecting 4 pieces in any direction
- **Leaderboard**: Persistent high scores tracking across games
- **Colorful Console Interface**: Enhanced visual experience with colored output
- **Flexible Board Size**: Configurable game board (default 6x6)
- **Input Validation**: Robust error handling for user inputs

## 🤖 AI Strategy

The AI opponent uses a sophisticated decision-making algorithm:

1. **Offensive Play**: Prioritizes moves that maximize its own points
2. **Defensive Play**: Blocks player moves that would result in high scores
3. **Positional Strategy**: When no scoring opportunities exist, chooses columns closest to the center for better positioning

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Terminal/Command Prompt with color support

### Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the game:

```bash
python AssCool.py
```

### Usage

1. **Start the Game**: Run the Python file and enter your name (2-9 characters)
2. **Make Moves**: Enter column numbers (0 to 5 for default 6x6 board)
3. **Objective**: Connect 4 of your pieces (`o`) in any direction to score points
4. **Win Condition**: Player with the most points when the board is full wins

### Game Controls

- Enter column number (0-5) to drop your piece
- The piece will fall to the lowest available position in that column
- Game ends when all columns are full

## 📊 Scoring & Leaderboard

- Points are awarded for each set of 4 connected pieces
- Multiple connections can be formed in a single move
- High scores are automatically saved to `leaderBoard.txt`
- Top 20 scores are displayed at the end of each game
- Your current score is highlighted in blue

### Special Commands

- Enter `admin` as username to reset the leaderboard

## 🛠️ Configuration

To change the board size:
1. Open `AssCool.py`
2. Navigate to the `display_entry()` function
3. Modify the `game = FourInARow(6)` line (change `6` to desired size)

## 📁 Project Structure

```
Four-in-a-row/
├── AssCool.py          # Main game file
├── leaderBoard.txt     #  score storage
└── README.md          # This file
```

## 🎯 Game Classes

### `GameBoard`
- Manages the game state and board logic
- Handles piece placement and scoring
- Implements win condition checking
- Provides AI decision-making utilities

### `FourInARow`
- Controls game flow and player interactions
- Manages turn-based gameplay
- Handles leaderboard operations
- Provides user interface

## 🎨 Visual Features

- **Color-coded Players**: Blue for player, red for AI
- **Real-time Scoring**: Points displayed during gameplay
- **Formatted Leaderboard**: Clean, organized high score display
- **Interactive Interface**: Clear prompts and feedback

## 🐛 Known Issues

- Optimized for VSCode terminal (may not display colors properly in Python IDLE)
- Requires terminal with ANSI color support for best experience

## 👤 Author

**Ubayd Abdul Majit**
- UPI: uabd315
- Student ID: 765724280

## 📝 Notes

- The AI implementation was provided as part of the project requirements
- Game supports customizable board sizes through code modification
- Leaderboard persists between game sessions
- Input validation ensures smooth gameplay experience

## 🎮 How to Play

1. **Setup**: Enter your player name when prompted
2. **Gameplay**: 
   - Choose a column (0-5) to drop your piece
   - Pieces fall to the lowest available spot
   - Try to connect 4 pieces horizontally, vertically, or diagonally
3. **Scoring**: Points are awarded for each 4-piece connection
4. **Victory**: Player with the most points when board is full wins!

---
