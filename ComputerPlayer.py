import random
import math


class ComputerPlayer:
    def __init__(self, player, computer_symbol):
        self.player = player
        self.computer_symbol = computer_symbol

    def find_best_move(self, board: list) -> list:
        best_evaluation = self.initialize_best_evaluation(self.computer_symbol)

        possible_moves = self.get_random_possible_moves(board)

        for possible_move in possible_moves:
            board[possible_move[0]][possible_move[1]] = self.computer_symbol
            current_move_evaluation = self.mini_max(
                board, self.next_player(self.computer_symbol)
            )
            board[possible_move[0]][possible_move[1]] = 0

            if self.is_maximizing(self.computer_symbol):
                if current_move_evaluation > best_evaluation:
                    best_evaluation = current_move_evaluation
                    best_move = [possible_move[0], possible_move[1]]
            else:
                if current_move_evaluation < best_evaluation:
                    best_evaluation = current_move_evaluation
                    best_move = [possible_move[0], possible_move[1]]

        return best_move

    def mini_max(self, board: list, player: str) -> int:
        current_move_evaluation = self.check_for_winner(board)

        if current_move_evaluation is not None:
            return current_move_evaluation

        min_max_evaluation = self.initialize_best_evaluation(player)

        for possible_move in self.get_ordered_possible_moves(board):
            board[possible_move[0]][possible_move[1]] = player
            current_move_evaluation = self.mini_max(board, self.next_player(player))
            board[possible_move[0]][possible_move[1]] = 0

            min_max_evaluation = self.calculate_min_max_evaluation(
                current_move_evaluation, min_max_evaluation, player
            )

        return min_max_evaluation

    def check_for_winner(self, board):
        winner = None
        scores = {"tie": 0, "X": 1, "O": -1}

        for row in board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]
                break

        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
                winner = board[0][col]
                break

        if (
            board[0][0] == board[1][1] == board[2][2]
            or board[0][2] == board[1][1] == board[2][0]
        ):
            if board[1][1] != 0:
                winner = board[1][1]

        if all([all(row) for row in board]) and winner is None:
            winner = "tie"

        if winner != None:
            return scores[winner]

    def get_random_possible_moves(self, board: list) -> list:
        possible_moves = self.get_ordered_possible_moves(board)

        random.shuffle(possible_moves)

        return possible_moves

    def get_ordered_possible_moves(self, board: list) -> list:
        possible_moves = [
            (row, col) for row in range(3) for col in range(3) if board[row][col] == 0
        ]

        return possible_moves

    def is_maximizing(self, player: str) -> bool:
        return player == "X"

    def next_player(self, current_player: str) -> str:
        return {"X": "O", "O": "X"}[current_player]

    def initialize_best_evaluation(self, player: str) -> int:
        return {"X": -math.inf, "O": math.inf}[player]

    def calculate_min_max_evaluation(
        self, current_move_evaluation: int, min_max_evaluation: int, player: str
    ) -> int:
        return {
            "X": max(current_move_evaluation, min_max_evaluation),
            "O": min(current_move_evaluation, min_max_evaluation),
        }[player]
