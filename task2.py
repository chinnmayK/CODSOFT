import tkinter as tk
from tkinter import messagebox

# Initialize board with empty cells
EMPTY = ''
PLAYER_X = 'X'
PLAYER_O = 'O'

# Create the game window using tkinter
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.root.configure(bg='#222222')
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.buttons = [[None] * 3 for _ in range(3)]
        self.player = PLAYER_X
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 40, 'bold'), width=5, height=2,
                                   bg='#1C1C1C', fg='#00FF41', activebackground='#1C1C1C',
                                   activeforeground='#00FF41', borderwidth=0, highlightthickness=0,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        # If the cell is empty, the human plays
        if self.board[i][j] == EMPTY:
            self.board[i][j] = PLAYER_X
            self.buttons[i][j].config(text=PLAYER_X, disabledforeground='#00FF41', state=tk.DISABLED)
            
            # Check if the game ends after the human's move
            if self.is_winner(PLAYER_X):
                self.game_over("You win!")
                return
            elif self.is_full():
                self.game_over("It's a draw!")
                return
            
            # Let the AI make its move
            self.ai_move()

    def ai_move(self):
        # AI (O) uses Minimax with Alpha-Beta Pruning
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_O
                    score = self.minimax(0, False, float('-inf'), float('inf'))
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        # Perform the best move
        if best_move:
            i, j = best_move
            self.board[i][j] = PLAYER_O
            self.buttons[i][j].config(text=PLAYER_O, disabledforeground='#FF5733', state=tk.DISABLED)

            # Check if the game ends after AI's move
            if self.is_winner(PLAYER_O):
                self.game_over("AI wins!")
            elif self.is_full():
                self.game_over("It's a draw!")

    def minimax(self, depth, is_maximizing, alpha, beta):
        # Base cases for recursion
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
        # Check rows, columns, and diagonals for a win
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
        # Display game over message and reset the board
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
