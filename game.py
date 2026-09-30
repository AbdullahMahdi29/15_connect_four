from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()

            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()
                if raw == "q":
                    return

                try:
                    col_input = int(raw)
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 7.")
                    continue

                if not 1 <= col_input <= 7:
                    print("Invalid column. Please choose a column between 1 and 7.")
                    continue

                col = col_input - 1
            else:
                col = self.ai.choose_column(self.board)
                if col is None:
                    # No legal moves left for AI -> Board is full without a winner
                    print("Draw.")
                    return

            # Attempt to drop the token
            if self.board.drop(col, self.turn) is None:
                print("Column unavailable.")
                continue

            # Move feedback: printed exactly once per confirmed move
            print(f"{self.turn} dropped in column {col + 1}.")

            # Win check
            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            # Draw check
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            # Switch turns
            self.turn = "O" if self.turn == "X" else "X"