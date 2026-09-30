import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(7) if board.grid[0][c] == "."]
        if not legal:
            return None

        # Priority 1: WIN
        # Check if AI can win immediately on this turn
        for col in legal:
            row = board.drop(col, me)
            if board.winner(me):
                board.grid[row][col] = "."  # Undo simulated move
                return col
            board.grid[row][col] = "."  # Undo simulated move

        # Priority 2: BLOCK
        # Check if opponent has an immediate winning threat to block
        for col in legal:
            row = board.drop(col, opponent)
            if board.winner(opponent):
                board.grid[row][col] = "."  # Undo simulated move
                return col
            board.grid[row][col] = "."  # Undo simulated move

        # Priority 3: OTHERWISE
        # Fall back safely to any available legal column
        return random.choice(legal)