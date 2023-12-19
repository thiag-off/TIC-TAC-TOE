from views import GameView
from controllers.game_manager import GameManager
from models import Game, Board, ComputerPlayer


class GameCreator:
    def __init__(self, master, create_screen, human_symbol, computer_player_enabled):
        self.master = master
        self.create_screen = create_screen
        self.human_symbol = human_symbol
        self.computer_player_enabled = computer_player_enabled

        self.board = Board()
        self.game = Game(self.board)

        if self.computer_player_enabled:
            self.computer_player = ComputerPlayer(self.human_symbol)
            self.game.set_computer_player(self.computer_player)

        self.game_view = GameView(self.master, self.create_screen)
        self.game_manager = GameManager(self.game, self.game_view)
