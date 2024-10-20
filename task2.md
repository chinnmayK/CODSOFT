# Tic-Tac-Toe AI Project

This project implements a Tic-Tac-Toe game where a human player can compete against an AI. The AI uses the Minimax algorithm with Alpha-Beta pruning to ensure it plays optimally, making it an unbeatable opponent. The game also features customizable themes: Dark, Light, and Neon.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Required Libraries**: 
  - Tkinter (included with Python standard library)

You do not need to install any additional libraries, as the project uses built-in modules.

---

## Project Structure

- **`task2.py`**: The main script that runs the Tic-Tac-Toe game.

---

## Installation Instructions

1. **Clone the repository**:
   Download or clone this repository to your local machine.

2. **Run the script**:
   Execute `task2.py` to start the game.

---

## Gameplay

### 1. Start the Game

Run the script to display the main menu, where you can select the difficulty level (Noob, Player, or Hacker).

### 2. Select Difficulty Level

Choose one of the following options:
- **Noob**: AI makes random moves.
- **Player**: AI has a 50% chance of making a random move and a 50% chance of making an optimal move.
- **Hacker**: AI plays optimally using the Minimax algorithm.

### 3. Customize Theme

You can access the settings to change the game theme. The available themes are:
- **Dark**: A dark color scheme with high contrast.
- **Light**: A bright and clean color scheme.
- **Neon**: A vibrant color scheme with neon effects.

### 4. Play the Game

- Click on the grid to place your move (X).
- The AI will respond with its move (O) after a brief loading animation.
- The game ends when a player wins or if the board is full, resulting in a draw.

---

## Acknowledgments

- **Tkinter**: For creating the graphical user interface.
- **Minimax Algorithm**: For the AI's decision-making process, ensuring optimal gameplay.

---