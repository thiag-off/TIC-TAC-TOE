from views import BoardGUI
from models import Game


class GameManager:
    def __init__(self, game: object, board_GUI: object):
        self.game = game
        self.board_GUI = board_GUI

        self.game.set_manager(self)
        self.board_GUI.set_manager(self)

        self.set_game()

    def update(self):
        self.board_GUI.update_button()

    def declare(self):
        self.board_GUI.declare_winner()

    def set_game(self):
        self.game.set_game()

    def handle_click(self, row, col):
        self.game.handle_click(row, col)

    def get_last_move_made(self):
        return self.game.get_last_move_made()

    def get_winner(self):
        return self.game.get_winner()
