import copy

from models import Board


class Game:
    def __init__(self, game_board: Board):
        self.game_board = game_board
        self.player = ["X", "O"]
        self.computer_player_enabled = False

        self.current_player: str
        self.last_move_made: str
        self.computer_role: str
        self.winner: str

        self.game_manager: object
        self.computer_player: object

    def set_computer_player(self, computer_player: object):
        self.computer_player = computer_player
        self.computer_player_enabled = True
        self.computer_role = self.computer_player.get_computer_role()

    def set_manager(self, manager: object):
        self.game_manager = manager

    def set_game(self):
        self.last_move_made = None
        self.winner = None
        self.game_board.set_default()
        self.current_player = self.player[0]

        if self.computer_player_enabled and self.computer_role == self.current_player:
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
                    self.computer_player_enabled
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
