class GameManager:
    def __init__(self, game: object, game_view: object):
        self.game = game
        self.game_view = game_view

        self.game.set_manager(self)
        self.game_view.set_manager(self)

        self.set_game()

    def update(self):
        self.game_view.update_button()

    def declare(self):
        self.game_view.declare_winner()

    def set_game(self):
        self.game.set_game()

    def handle_click(self, row, col):
        self.game.handle_click(row, col)

    def get_last_move_made(self):
        return self.game.get_last_move_made()

    def get_winner(self):
        return self.game.get_winner()
