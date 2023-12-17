from views import BoardGUI
from controllers.game_manager import GameManager
from models import Game


class GameCreator:
    def __init__(self, master, create_screen, player_symbol, opponent_type):
        self.master = master
        self.create_screen = create_screen
        self.player_symbol = player_symbol
        self.opponent_type = opponent_type

        self.game = Game(self.player_symbol, self.opponent_type)
        self.board_GUI = BoardGUI(self.master, self.create_screen)
        self.game_manager = GameManager(self.game, self.board_GUI)
