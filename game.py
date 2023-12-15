import random
from ComputerPlayer import ComputerPlayer
from Board import Board
import copy


class Game:
    def __init__(self, update_button, declare_winner, player_symbol, opponent_type):
        self.player_symbol = player_symbol
        self.player = ["X", "O"]
        self.computer_role = (
            self.player[0] if player_symbol == self.player[1] else self.player[1]
        )
        self.computer_player = ComputerPlayer(self.player, self.computer_role)
        self.is_computer_player_enabled = opponent_type == "Computer"
        self.update_button_callback = update_button
        self.declare_winner_callback = declare_winner
        self.set_game()

    def set_game(self):
        self.winner = None
        self.game_board = Board()
        self.current_player = self.player[0]

        if (
            self.is_computer_player_enabled
            and self.computer_role == self.current_player
        ):
            self.computer_move()

    def computer_move(self):
        move = self.computer_player.find_best_move(copy.copy(self.game_board))
        self.handle_click(move[0], move[1])

    def handle_click(self, row, col):
        if self.game_board.is_cell_empty(row, col):
            self.game_board.mark(row, col, self.current_player)
            self.update_button_callback(row, col, self.game_board.get_cell(row, col))
            self.switch_turn()
            self.check_for_winner()

            if (
                self.is_computer_player_enabled
                and self.computer_role == self.current_player
                and not self.winner
            ):
                self.computer_move()

    def check_for_winner(self):
        self.winner = self.game_board.check_for_winner()

        if self.winner:
            self.declare_winner_callback(self.winner)

    def switch_turn(self):
        self.current_player = {
            self.player[0]: self.player[1],
            self.player[1]: self.player[0],
        }[self.current_player]

    def is_cell_empty(self, row, col):
        return self.board[row][col] in [0]
