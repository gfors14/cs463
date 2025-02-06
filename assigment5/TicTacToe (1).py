import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeBackend:
    def __init__(self):
        #Initializes the backend with an empty board and player symbols
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.computer = "O"  # Computer is always "O"
        self.human = "X"  # Human player is always "X"

    def reset_board(self):
        #Reset the game board
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        #Make a move on the board
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def is_winner(self, player):
        #Checks if the given player has won
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        #Checks if the game is a draw
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))

    def get_empty_cells(self):
        #Get a list of all empty cells.
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

    def find_winning_move(self, player):
        #Find a winning move for the given player, if it exists.
        for row, col in self.get_empty_cells():
            self.board[row][col] = player
            if self.is_winner(player):
                self.board[row][col] = " "  # Undo the move
                return row, col
            self.board[row][col] = " "  # Undo the move
        return None

    def make_ai_move(self):
        #AI logic for the computer's move
        # Step 1: First move - center
        if all(self.board[row][col] == " " for row in range(3) for col in range(3)):
            self.board[1][1] = self.computer
            return 1, 1

        # Step 2: Check if AI can win in one move
        winning_move = self.find_winning_move(self.computer)
        if winning_move:
            self.board[winning_move[0]][winning_move[1]] = self.computer
            return winning_move

        # Step 3: If the AI can't win in a single move the AI will attempt to block the player
        blocking_move = self.find_winning_move(self.human)
        if blocking_move:
            self.board[blocking_move[0]][blocking_move[1]] = self.computer
            return blocking_move

        # Step 4: If the AI can't win or block the player they will play a random empty cell
        empty_cells = self.get_empty_cells()
        if empty_cells:
            row, col = random.choice(empty_cells)  # Choose a random move
            self.board[row][col] = self.computer
            return row, col

        return None


class TicTacToeUI:
    def __init__(self, root):
        #Initializea the UI and link it with the backend
        self.root = root
        self.root.title("Tic Tac Toe")
        self.backend = TicTacToeBackend()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.current_player = "O"  # Computer goes first
        self.computer_move()

    def create_board(self):
        #Creates the game board UI
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root, text="", font=("Arial", 24),
                    width=5, height=2,
                    command=lambda r=row, c=col: self.handle_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        #Handle user click on the board
        if self.current_player != "X":  # Ignore clicks when it's not the user's turn
            return
        if not self.backend.make_move(row, col, "X"):  # Ignore invalid moves
            return

        self.buttons[row][col].config(text="X")
        if self.check_game_state("X"):
            return

        self.current_player = "O"
        self.computer_move()

    def computer_move(self):
        #Handle the computer's move
        row, col = self.backend.make_ai_move()
        self.buttons[row][col].config(text="O")
        if self.check_game_state("O"):
            return
        self.current_player = "X"

    def check_game_state(self, player):
        #Checks the game state for a winner or draw
        if self.backend.is_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            self.reset_game()
            return True
        if self.backend.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        #Resets the game board
        self.backend.reset_board()
        self.current_player = "O"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.computer_move()


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()

