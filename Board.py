class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def handle_click(self, player):
        if self.is_cell_empty():
            self.mark_board(row, col, player)

    def check_for_winner(self) -> str:
        winner = None
        # check columns
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]
                return winner
        # check rows
        for col in range(len(self.board)):
            if (
                self.board[0][col] == self.board[1][col] == self.board[2][col]
                and self.board[0][col] != 0
            ):
                winner = self.board[0][col]
                return winner
        # check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2]
            or self.board[0][2] == self.board[1][1] == self.board[2][0]
        ):
            if self.board[1][1] != 0:
                winner = self.board[1][1]
                return winner
        # check tie
        if all([all(row) for row in self.board]) and winner is None:
            winner = "tie"
            return winner

    def is_cell_empty(self, row: int, col: int) -> bool:
        return self.get_cell(row, col) in [0]

    def get_cell(self, row: int, col: int) -> str | int:
        return self.board[row][col]

    def mark_board(self, row: int, col: int, player: str) -> None:
        self.board[row][col] = player

    def unmark_board(self, row: int, col: int, player: str) -> None:
        self.board[row][col] = 0

    def find_all_empty_cells(self) -> list:
        return [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.is_cell_empty(row, col)
        ]

    def get_board(self) -> list:
        return self.board
