import tkinter as tk

class ChessBoardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Board")
        self.geometry("530x550")
        self.create_board()

    def create_board(self):
        self.board = []
        for row in range(8):
            current_row = []
            for col in range(8):
                color = "#FFFFE4" if (row + col) % 2 == 0 else "#231709"
                square = tk.Frame(self, width=60, height=60, bg=color)
                square.grid(row=row, column=col, padx=1, pady=1)
                square.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))
                current_row.append(square)
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

    def on_square_click(self, row, col):
        print(f"Clicked square: {chr(97 + col)}{8 - row}")  # Example: converts 0-7 to 'a'-'h' and 0-7 to '8'-'1'

if __name__ == "__main__":
    app = ChessBoardApp()
    app.mainloop()
