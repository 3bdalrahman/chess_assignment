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
        ['', '', '', 'b', '', 'r', '', ''],
        ['', '', '', '', 'P', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', 'K', '']
    ],
    # Puzzle 2
    [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', 'b', '', 'b', '', ''],
        ['', '', '', '', 'P', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', 'K', '']
    ],
    # Puzzle 3
    [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', 'r', '', 'b', '', ''],
        ['', '', '', '', 'P', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'P', 'P', 'P'],
        ['', '', '', '', '', '', 'K', '']
    ]
]

class ChessPuzzle(tk.Frame):
    def __init__(self, parent, puzzle):
        super().__init__(parent)
        self.parent = parent
        self.puzzle = puzzle
        self.original_puzzle = [row[:] for row in puzzle]  # Create a copy of the original puzzle
        self.piece_scores = {'p': 1, 'n': 3, 'b': 4, 'r': 5, 'q': 9}
        self.create_board()
        self.moves_executed = False

    def highlight_possible_moves(self):
        white_pawns = self.detect_white_pawns()

        for pawn_position in white_pawns:
            legal_moves_with_pieces = self.detect_legal_moves_with_pieces(pawn_position)
            best_move = self.find_best_move(legal_moves_with_pieces)
            self.highlight_moves(legal_moves_with_pieces, best_move)

    def highlight_moves(self, legal_moves_with_pieces, best_move):
        for move, piece in legal_moves_with_pieces:
            row, col = move
            square_frame = self.squares[row][col]

            # Change background color to red for best move
            if best_move:
                row, col = best_move
                square_frame = self.squares[row][col]
                for widget in square_frame.winfo_children():
                    widget.config(bg="red")

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

                row_squares.append(square)
            self.squares.append(row_squares)

        # Create start and undo buttons
        self.start_button = tk.Button(self, text="Move", command=self.start_puzzle)
        self.start_button.grid(row=9, column=0, columnspan=4, sticky='we', padx=5, pady=5)
        self.undo_button = tk.Button(self, text="Undo", command=self.undo_move, state=tk.DISABLED)
        self.undo_button.grid(row=9, column=4, columnspan=4, sticky='we', padx=5, pady=5)

    def evaluate_move(self, row, col):
        """
        Evaluate a move based on the scoring system:
        - Capture: +1
        - Move forward: 0
        - Move backward: -1
        """
        if not (0 <= row < 8 and 0 <= col < 8):
            return -1  # Invalid move (move backward)

        piece_char = self.puzzle[row][col]
        if piece_char == 'P':
            return 0  # Move forward
        elif piece_char in ('r', 'n', 'b', 'q', 'k', 'p'):
            return 1  # Capture
        else:
            return -1  # Empty square (move backward)

    def find_best_moves(self):
        if not self.moves_executed:
            white_pawns = self.detect_white_pawns()

            for pawn_position in white_pawns:
                legal_moves_with_pieces = self.detect_legal_moves_with_pieces(pawn_position)
                best_move = self.find_best_move(legal_moves_with_pieces)
                if best_move:
                    self.execute_move(pawn_position, best_move)
                    self.moves_executed = True

    def find_best_move(self, legal_moves_with_pieces):
        best_score = float('-inf')
        best_move = None

        for move, piece in legal_moves_with_pieces:
            if piece.islower():
                score = self.piece_scores.get(piece.lower(), 0)
                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move

    def execute_move(self, pawn_position, best_move):
        row, col = pawn_position
        new_row, new_col = best_move

        self.puzzle[row][col] = ' '  # Remove the pawn from its current position
        self.puzzle[new_row][new_col] = 'P'  # Move the pawn to the best move position
        self.update_display()  # Update the display after moving

    def detect_white_pawns(self):
        white_pawn_positions = []
        for row in range(8):
            for col in range(8):
                piece = self.puzzle[row][col]
                if piece == 'P':  # 'P' represents a white pawn
                    white_pawn_positions.append((row, col))
        return white_pawn_positions

    def detect_legal_moves_with_pieces(self, pawn_position):
        legal_moves_with_pieces = []
        row, col = pawn_position
        # Check if the pawn can move one square forward
        if row > 0 and self.puzzle[row - 1][col] == ' ':
            legal_moves_with_pieces.append(((row - 1, col), self.puzzle[row - 1][col]))
        # Check if the pawn can move diagonally left to capture an opponent's piece
        if row > 0 and col > 0 and self.puzzle[row - 1][col - 1] != ' ':
            legal_moves_with_pieces.append(((row - 1, col - 1), self.puzzle[row - 1][col - 1]))
        # Check if the pawn can move diagonally right to capture an opponent's piece
        if row > 0 and col < 7 and self.puzzle[row - 1][col + 1] != ' ':
            legal_moves_with_pieces.append(((row - 1, col + 1), self.puzzle[row - 1][col + 1]))
        return legal_moves_with_pieces

    def update_display(self):
        for row_idx, row in enumerate(self.puzzle):
            for col_idx, piece_char in enumerate(row):
                square_frame = self.squares[row_idx][col_idx]
                for widget in square_frame.winfo_children():
                    widget.destroy()

                if piece_char:
                    color = "#FFFFE4" if (row_idx + col_idx) % 2 == 0 else "#7ABA78"
                    label_piece = tk.Label(square_frame, text=UNICODE_PIECES.get(piece_char, ''), font=("Arial", 36),
                                           bg=color)
                    label_piece.place(relx=0.5, rely=0.5, anchor='center')  # Center the label within the square

    def start_puzzle(self):
        self.find_best_moves()
        self.start_button.grid_forget()  # Hide the start button
        self.undo_button.config(state=tk.NORMAL)  # Enable the undo button

    def undo_move(self):
        # Restore the puzzle to its original state
        for i in range(8):
            for j in range(8):
                self.puzzle[i][j] = self.original_puzzle[i][j]
        self.update_display()  # Update the display after undoing the move
        self.moves_executed = False
        self.start_button.grid(row=9, column=0, columnspan=4, sticky='we', padx=5, pady=5)  # Show the start button
        self.undo_button.config(state=tk.DISABLED)  # Disable the undo button

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.notebook = None
        self.title("Chess Puzzles")
        self.geometry("490x600")  # Increased height to accommodate the button
        self.create_notebook()

    def create_notebook(self):
        # Create notebook widget to hold puzzle pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Create puzzle pages within the notebook
        for i, puzzle_data in enumerate(PUZZLES):
            page = ChessPuzzle(self.notebook, puzzle_data)
            self.notebook.add(page, text=f'Puzzle {i+1}')

        # Create an Analysis button
        analysis_button = tk.Button(self, text="Analysis", command=self.analyze_moves)
        analysis_button.pack(side='bottom')


    def analyze_moves(self):
        # Analyze and highlight possible moves
        selected_index = self.notebook.index(self.notebook.select())
        puzzle_frame = self.notebook.winfo_children()[selected_index]
        puzzle_frame.highlight_possible_moves()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
