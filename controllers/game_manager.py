from views import BoardGUI
from models import Game


class GameManager:

    def __init__(self, master, create_screen, player_symbol, opponent_type):
        self.player_symbol = player_symbol
        self.opponent_type = opponent_type
        self.master = master
        self.create_screen = create_screen

        self.game = Game(self.player_symbol, self.opponent_type, self)
        self.board_GUI = BoardGUI(self.master, self, self.create_screen)
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

