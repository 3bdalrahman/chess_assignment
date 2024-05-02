import tkinter as tk

# Unicode chess pieces dictionary
UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

class ChessBoardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Board")
        self.geometry("530x550")
        self.create_board()

    def create_board(self):
        self.board = []
        square_size = 60  # Size of each square

        for row in range(8):
            current_row = []
            for col in range(8):
                color = "#FFFFE4" if (row + col) % 2 == 0 else "red"
                square = tk.Frame(self, width=square_size, height=square_size, bg=color)
                square.grid(row=row, column=col, padx=1, pady=1)
                current_row.append(square)

                # Display pieces on the board (starting position)
                piece_char = UNICODE_PIECES.get(self.initial_board_position(row, col), '')
                if piece_char:
                    label_piece = tk.Label(square, text=piece_char, font=("Arial", 36), bg=color)
                    label_piece.pack(fill='both', expand=True)  # Ensure label fills the square
                    label_piece.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))

            self.board.append(current_row)

        # Labels for file (a-h) and rank (1-8)
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ranks = ['8', '7', '6', '5', '4', '3', '2', '1']

        for col in range(8):
            label_file = tk.Label(self, text=files[col], bg="white", width=7, height=3, padx=0, pady=0)
            label_file.grid(row=8, column=col, padx=1, pady=1, sticky="ew")

        for row in range(8):
            label_rank = tk.Label(self, text=ranks[row], bg="white", width=3, height=2, padx=0, pady=0)
            label_rank.grid(row=row, column=8, padx=1, pady=1, sticky="ns")

    def initial_board_position(self, row, col):
        # Return the piece abbreviation for the initial chessboard setup
        if row == 1:
            return 'P'  # White pawn (second row)
        elif row == 6:
            return 'p'  # Black pawn (seventh row)
        elif row == 0 or row == 7:
            pieces_row = 'RNBQKBNR' if row == 0 else 'rnbqkbnr'
            return pieces_row[col]  # Return corresponding piece for first and eighth row
        else:
            return None  # Empty square for other rows

    def on_square_click(self, row, col):
        # Handle square click event
        print(f"Clicked square: {chr(97 + col)}{8 - row}")  # Example: converts 0-7 to 'a'-'h' and 0-7 to '8'-'1'

if __name__ == "__main__":
    app = ChessBoardApp()
    app.mainloop()
