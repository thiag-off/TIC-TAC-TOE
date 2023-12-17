import copy

from models import ComputerPlayer, Board


class Game:
    def __init__(self, player_symbol, opponent_type):
        self.game_board = None
        self.current_player = None
        self.last_move_made = None
        self.player_symbol = player_symbol
        self.player = ["X", "O"]
        self.computer_role = (
            self.player[0] if player_symbol == self.player[1] else self.player[1]
        )
        self.computer_player = ComputerPlayer(self.player, self.computer_role)
        self.is_computer_player_enabled = opponent_type == "Computer"
        self.game_manager: object

        self.winner = None

    def set_manager(self, manager: object):
        self.game_manager = manager

    def set_game(self):
        self.last_move_made = None
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
            self.last_move_made = [row, col, self.game_board.get_cell(row, col)]
            self.game_manager.update()
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
            self.game_manager.declare()

    def switch_turn(self):
        self.current_player = {
            self.player[0]: self.player[1],
            self.player[1]: self.player[0],
        }[self.current_player]

    def get_current_player(self):
        return self.current_player

    def get_winner(self):
        return self.winner

    def get_last_move_made(self):
        return self.last_move_made
