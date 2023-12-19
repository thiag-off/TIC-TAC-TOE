import random
import math

from models.board import Board


class ComputerPlayer:
    def __init__(self, human_symbol):
        self.player = ["X", "O"]
        self.computer_symbol = {"X": "O", "O": "X"}[human_symbol]

    def find_best_move(self, board: Board) -> list:
        best_evaluation = self.initialize_best_evaluation(self.computer_symbol)

        possible_moves = self.get_random_possible_moves(board)

        for possible_move in possible_moves:
            board.mark(possible_move[0], possible_move[1], self.computer_symbol)
            current_move_evaluation = self.mini_max(
                board, self.next_player(self.computer_symbol)
            )

            board.unmark(possible_move[0], possible_move[1])

            if self.is_maximizing(self.computer_symbol):
                if current_move_evaluation > best_evaluation:
                    best_evaluation = current_move_evaluation
                    best_move = [possible_move[0], possible_move[1]]
            else:
                if current_move_evaluation < best_evaluation:
                    best_evaluation = current_move_evaluation
                    best_move = [possible_move[0], possible_move[1]]

        return best_move

    def mini_max(self, board: Board, player: str) -> int:
        current_move_evaluation = self.check_for_winner(board)

        if current_move_evaluation is not None:
            return current_move_evaluation

        min_max_evaluation = self.initialize_best_evaluation(player)

        for possible_move in self.get_ordered_possible_moves(board):
            board.mark(possible_move[0], possible_move[1], player)
            current_move_evaluation = self.mini_max(board, self.next_player(player))
            board.unmark(possible_move[0], possible_move[1])

            min_max_evaluation = self.calculate_min_max_evaluation(
                current_move_evaluation, min_max_evaluation, player
            )

        return min_max_evaluation

    def check_for_winner(self, board: Board):
        winner = board.check_for_winner()
        scores = {"tie": 0, "X": 1, "O": -1}

        if winner is not None:
            return scores[winner]

    def get_random_possible_moves(self, board: Board) -> list:
        possible_moves = self.get_ordered_possible_moves(board)

        random.shuffle(possible_moves)

        return possible_moves

    def get_ordered_possible_moves(self, board: Board) -> list:
        return board.find_all_empty_cells()

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

    def get_computer_role(self):
        return self.computer_symbol
