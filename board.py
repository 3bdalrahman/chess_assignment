import tkinter as tk
from tkinter import ttk
import random

# Unicode chess pieces dictionary
UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

# Function to generate a random puzzle
def generate_random_puzzle():
    # Initialize an empty 8x8 board
    puzzle = [['' for _ in range(8)] for _ in range(8)]

    # Place random pieces on the board
    for _ in range(10):  # Let's say we want to place 10 pieces randomly
        piece = random.choice(list(UNICODE_PIECES.values()))
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        puzzle[row][col] = piece

    return puzzle


class ChessPuzzle(tk.Frame):
    def __init__(self, parent, puzzle):
        super().__init__(parent)
        self.puzzle = puzzle
        self.create_board()

    def create_board(self):
        square_size = 55  # Size of each square
        for row in range(8):
            for col in range(8):
                color = "#FFFFE4" if (row + col) % 2 == 0 else "#7ABA78"
                square = tk.Frame(self, width=square_size, height=square_size, bg=color)
                square.grid(row=row, column=col, padx=1, pady=1)

                piece_char = self.puzzle[row][col]
                if piece_char:
                    label_piece = tk.Label(square, text=piece_char, font=("Arial", 36), bg=color)
                    label_piece.pack(fill='both', expand=True)

# Predefined puzzles
PUZZLES = [
    # Puzzle 1
    [
        ['r', '', '', '', '', 'k', '', ''],
        ['', 'p', '', '', '', '', '', ''],
        ['', '', '', '', 'P', 'P', 'P', ''],
        ['p', '', '', '', '', 'N', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['P', '', '', '', '', '', '', ''],
        ['', 'P', '', '', '', '', '', ''],
        ['K', '', '', '', '', '', '', '']
    ],
    # Puzzle 2
    [
        ['', '', '', '', '', '', '', ''],
        ['p', '', '', '', '', '', '', ''],
        ['', 'p', '', '', '', '', 'p', ''],
        ['k', 'P', '', '', '', '', 'P', 'p'],
        ['', '', 'P', '', '', '', '', 'P'],
        ['', 'P', '', '', '', '', '', ''],
        ['', 'K', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '']
    ],
    # Puzzle 3
    [
        ['', '', '', '', '', '', 'K', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', '', '', ''],
        ['b', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '']
    ]
]

def generate_static_puzzle(puzzle_number):
    # Convert piece abbreviations to unicode characters
    return [[UNICODE_PIECES.get(piece, '') for piece in row] for row in PUZZLES[puzzle_number]]

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Puzzles")
        self.geometry("490x570")  # Adjust if necessary
        self.create_notebook()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Create three static puzzles
        for i in range(3):
            puzzle_data = generate_static_puzzle(i)  # Ensure this returns a valid puzzle
            page = ChessPuzzle(self.notebook, puzzle_data)
            self.notebook.add(page, text=f'Puzzle {i+1}')  # Check tabs are added correctly

        # Start button at the bottom
        start_button = tk.Button(self, text="Start", command=self.start_puzzle)
        start_button.pack(side='bottom')  # Check button is visible

    def start_puzzle(self):
        # Implement puzzle starting logic
        pass

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()  # Ensure this is called
