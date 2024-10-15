import tkinter as tk
from tkinter import messagebox
import random  # Import random for AI moves

# Initialize board with empty cells
EMPTY = ''
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define color themes
THEMES = {
    "Dark": {"bg": "#222222", "fg": "#00FF41", "button_bg": "#1C1C1C", "circle_fg": "#FF5733"},
    "Light": {"bg": "#FFFFFF", "fg": "#000000", "button_bg": "#F0F0F0", "circle_fg": "#FF5733"},
    "Neon": {"bg": "#2E003E", "fg": "#39FF14", "button_bg": "#1C1C1C", "circle_fg": "#FFD700"}
}

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.theme = "Dark"  # Default theme

        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.buttons = [[None] * 3 for _ in range(3)]  # Initialize buttons as empty 2D array
        self.player = PLAYER_X
        self.difficulty = None

        self.create_settings_button()
        self.create_difficulty_selection()

    def create_settings_button(self):
        settings_button = tk.Button(self.root, text="Settings", font=('Arial', 14), command=self.open_settings)
        settings_button.grid(row=4, column=0, columnspan=3, pady=10)

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")

        label = tk.Label(settings_window, text="Select Theme:", font=('Arial', 16))
        label.pack(pady=10)

        # Theme selection buttons
        for theme_name in THEMES:
            tk.Button(settings_window, text=theme_name, font=('Arial', 14),
                      command=lambda t=theme_name: self.apply_theme(t, settings_window)).pack(pady=5)

    def apply_theme(self, theme_name, settings_window):
        self.theme = theme_name
        self.set_theme(THEMES[self.theme])
        settings_window.destroy()

    def set_theme(self, theme):
        self.root.configure(bg=theme["bg"])
        self.theme_settings = theme  # Store current theme settings

        # Update all buttons and labels with the new theme
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]:
                    self.buttons[i][j].config(bg=self.theme_settings["button_bg"],
                                              fg=self.theme_settings["fg"],
                                              activebackground=self.theme_settings["button_bg"],
                                              activeforeground=self.theme_settings["fg"])
        # Change the color of the Settings button if it exists
        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Button) and widget["text"] == "Settings":
                widget.config(bg=self.theme_settings["button_bg"], fg=self.theme_settings["fg"])

    def create_difficulty_selection(self):
        # Create buttons to select difficulty level before starting
        label = tk.Label(self.root, text="Select Difficulty Level", font=('Arial', 20),
                         bg=THEMES[self.theme]["bg"], fg=THEMES[self.theme]["fg"])
        label.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="Noob", font=('Arial', 20), bg=THEMES[self.theme]["button_bg"],
                  fg=THEMES[self.theme]["fg"], command=lambda: self.start_game("noob")).grid(row=1, column=0)
        tk.Button(self.root, text="Player", font=('Arial', 20), bg=THEMES[self.theme]["button_bg"],
                  fg=THEMES[self.theme]["fg"], command=lambda: self.start_game("player")).grid(row=1, column=1)
        tk.Button(self.root, text="Hacker", font=('Arial', 20), bg=THEMES[self.theme]["button_bg"],
                  fg=THEMES[self.theme]["fg"], command=lambda: self.start_game("hacker")).grid(row=1, column=2)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.clear_difficulty_selection()
        self.create_board()
        self.set_theme(THEMES[self.theme])  # Apply the theme after the board is created

    def clear_difficulty_selection(self):
        # Clear the difficulty selection screen
        for widget in self.root.grid_slaves():
            widget.grid_forget()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 40, 'bold'), width=5, height=2,
                                   bg=THEMES[self.theme]["button_bg"], fg=THEMES[self.theme]["fg"],
                                   activebackground=THEMES[self.theme]["button_bg"],
                                   activeforeground=THEMES[self.theme]["fg"], borderwidth=0, highlightthickness=0,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.board[i][j] == EMPTY:
            self.board[i][j] = PLAYER_X
            self.buttons[i][j].config(text=PLAYER_X, disabledforeground=self.theme_settings["fg"], state=tk.DISABLED)
            
            if self.is_winner(PLAYER_X):
                self.game_over("You win!")
                return
            elif self.is_full():
                self.game_over("It's a draw!")
                return
            
            # Show the loading circle jumping between remaining boxes
            self.empty_cells = [(x, y) for x in range(3) for y in range(3) if self.board[x][y] == EMPTY]
            self.current_index = 0
            self.show_loading_in_remaining_boxes()

    def show_loading_in_remaining_boxes(self):
        if self.current_index < len(self.empty_cells):
            i, j = self.empty_cells[self.current_index]
            self.buttons[i][j].config(text='○', fg=self.theme_settings["circle_fg"])  # Display circle in empty box

            if self.current_index > 0:
                prev_i, prev_j = self.empty_cells[self.current_index - 1]
                self.buttons[prev_i][prev_j].config(text='')

            self.current_index += 1
            self.root.after(70, self.show_loading_in_remaining_boxes)  # Faster loading speed (70ms)
        else:
            last_i, last_j = self.empty_cells[-1]
            self.buttons[last_i][last_j].config(text='')
            self.root.after(100, self.ai_move)  # AI makes its move after the animation

    def ai_move(self):
        if self.difficulty == "noob":
            # Noob mode: AI makes random moves, allowing the player to win
            best_move = random.choice(self.empty_cells)
        elif self.difficulty == "player":
            # Player mode: 50% chance of AI making a random move, 50% chance of making an optimal move
            if random.random() < 0.5:
                best_move = random.choice(self.empty_cells)
            else:
                best_move = self.get_optimal_move()
        else:
            # Hacker mode: AI plays optimally
            best_move = self.get_optimal_move()

        if best_move:
            i, j = best_move
            self.board[i][j] = PLAYER_O
            self.buttons[i][j].config(text=PLAYER_O, disabledforeground=self.theme_settings["circle_fg"], state=tk.DISABLED)

            if self.is_winner(PLAYER_O):
                self.game_over("AI wins!")
            elif self.is_full():
                self.game_over("It's a draw!")

    def get_optimal_move(self):
        best_score = float('-inf')
        best_move = None

        for i, j in self.empty_cells:
            self.board[i][j] = PLAYER_O
            score = self.minimax(0, False, float('-inf'), float('inf'))
            self.board[i][j] = EMPTY
            if score > best_score:
                best_score = score
                best_move = (i, j)
        
        return best_move

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.is_winner(PLAYER_X):
            return -1
        elif self.is_winner(PLAYER_O):
            return 1
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = PLAYER_O
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = EMPTY
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = PLAYER_X
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = EMPTY
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
        for j in range(3):
            if all(self.board[i][j] == player for i in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.board[i][j] != EMPTY for i in range(3) for j in range(3))

    def game_over(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_board()

    def reset_board(self):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
