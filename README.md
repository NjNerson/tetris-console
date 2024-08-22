# Tetris Game in Python (Console Version)

## Overview

This is a console-based Tetris game implemented in Python. The game runs in the terminal and features standard Tetris gameplay mechanics including moving pieces, rotating, and clearing lines. The game consists of three levels with varying piece fall speeds: normal, fast, and fast and furious.

## Features

- **4x4 Block Pieces:** Each Tetris piece is represented as a 4x4 block.
- **Game Grid:** The game board is 10 columns wide and 20 lines high.
- **Movement Controls:** Move pieces left, right, accelerate to the bottom, and rotate using direction keys.
- **Collision Management:** Pieces stop moving when they hit the bottom or other pieces.
- **Line Clearing:** Complete lines are cleared, and the score increases.
- **Levels:** Three levels with different fall speeds: normal, fast, and fast and furious.
- **Game Over:** The game ends when there is no space for a new piece.

## Installation

1. **Ensure Python 3.10 is installed:** This game is built using Python 3.10. Download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/njnerson/tetris-console.git
   cd tetris-console
   ```

3. **Install Dependencies:**
   This game does not require additional libraries outside the standard Python library.

## Usage

1. **Run the Game:**

   ```bash
   python main.py
   ```

2. **Game Controls:**
   - **Arrow Keys:** Move the piece left, right, or accelerate down.
   - **Up Arrow:** Rotate the piece.
   - **Space Bar:** Pause and resume the game.

## Code Structure

- **`main.py`:** Main file to run the game.
- **`utils/board.py`:** Contains the `Board` class which manages the game grid, piece movements, collisions, and scoring.
- **`utils/piece.py`:** Contains the `Piece` class to represent Tetris pieces and their rotations.
- **`utils/pause_handler.py`:** Manages the game pausing functionality.
- **`utils/config.py`:** Contains game configuration settings such as piece fall speeds.

## Example Gameplay

To start the game, run the following command:

```bash
python main.py
```

## Screenshot

![Application Screenshot](docs/tetris-console.png)

##

Use the arrow keys to control the pieces. The game will display the current score and level. The game ends when there is no space for a new piece to appear.
