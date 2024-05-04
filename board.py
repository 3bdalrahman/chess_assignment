import tkinter as tk
from tkinter import ttk

# Unicode chess pieces dictionary
UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

# Labels for file (a-h) and rank (1-8)
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = ['8', '7', '6', '5', '4', '3', '2', '1']

# Predefined puzzles
PUZZLES = [
    # Puzzle 1
    [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', '', 'r', 'b', '', ''],
        ['', '', '', '', '', 'P', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', '', 'K']
    ],
    # Puzzle 2
    [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', '', 'r', 'b', '', ''],
        ['', '', '', '', '', 'P', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', '', 'K']
    ],
    # Puzzle 3
    [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', '', 'r', 'b', '', ''],
        ['', '', '', '', '', 'P', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', '', 'K']
    ]
]

class ChessPuzzle(tk.Frame):
    def __init__(self, parent, puzzle):
        super().__init__(parent)
        self.puzzle = puzzle
        self.create_board()

    def create_board(self):
        square_size = 55  # Size of each square

        # Add labels for files (a-h)
        for col, file_label in enumerate(files):
            label_file = tk.Label(self, text=file_label, font=("Arial", 12), width=2, bg="#E6E6E6")
            label_file.grid(row=8, column=col, padx=1, pady=1)

        # Add labels for ranks (1-8)
        for row, rank_label in enumerate(ranks):
            label_rank = tk.Label(self, text=rank_label, font=("Arial", 12), height=2, bg="#E6E6E6")
            label_rank.grid(row=7-row, column=8, padx=1, pady=1)

        # Create squares for the chessboard
        self.squares = []  # List to store square widgets
        for row in range(8):
            row_squares = []
            for col in range(8):
                color = "#FFFFE4" if (row + col) % 2 == 0 else "#7ABA78"
                square = tk.Frame(self, width=square_size, height=square_size, bg=color)
                square.grid(row=row, column=col, padx=1, pady=1)

                piece_char = self.puzzle[row][col]
                if piece_char:
                    label_piece = tk.Label(square, text=UNICODE_PIECES.get(piece_char, ''), font=("Arial", 36), bg=color)
                    label_piece.pack(fill='both', expand=True)

                # Bind click event to the square using a closure to capture current row and col
                square.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))

                row_squares.append(square)
            self.squares.append(row_squares)

    def on_square_click(self, row, col):
        # Handle click event on chessboard square
        clicked_square_name = f'{files[col]}{ranks[7-row]}'  # Get square name (e.g., 'a1', 'h8')
        piece_char = self.puzzle[row][col]
        if piece_char:
            print(f"Clicked Square: {clicked_square_name}, Piece: {piece_char}")
        else:
            print(f"Clicked Square: {clicked_square_name}, Empty")

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Puzzles")
        self.geometry("490x570")  # Set initial window size
        self.create_notebook()

    def create_notebook(self):
        # Create notebook widget to hold puzzle pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Create puzzle pages within the notebook
        for i, puzzle_data in enumerate(PUZZLES):
            page = ChessPuzzle(self.notebook, puzzle_data)
            self.notebook.add(page, text=f'Puzzle {i+1}')

        # Create a dummy start button at the bottom
        start_button = tk.Button(self, text="Start", command=self.start_puzzle)
        start_button.pack(side='bottom')

    def start_puzzle(self):
        # Placeholder for puzzle starting logic
        pass

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
