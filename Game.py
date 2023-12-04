import random 
from ComputerPlayer import ComputerPlayer
class Game:
    def __init__(self, update_button, declare_winner, player_symbol, opponent_type):        

        self.player_symbol = player_symbol      
        self.player = ["X", "O"]
        self.computer_role = self.player[0] if player_symbol == self.player[1] else self.player[1]
        self.computer_player = ComputerPlayer(self.player, self.computer_role)
        self.is_computer_player_enabled = opponent_type == "Computer"
        self.update_button_callback = update_button
        self.declare_winner_callback = declare_winner
        self.set_game()
           
    def set_game(self):
        self.winner = None        
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.current_player = self.player[0]
             
        if self.is_computer_player_enabled and self.computer_role == self.current_player :
            self.computer_move()        
       

    def computer_move(self):
        move = self.computer_player.find_best_move(self.board[:])
        self.handle_click(move[0],move[1])
     
    def handle_click(self, row, col):        

        if self.is_cell_empty(row, col):
            self.board[row][col] = self.current_player
            self.update_button_callback(row,col, self.board[row][col])
            self.switch_turn()
            self.check_for_winner()           
           
            if self.is_computer_player_enabled and self.computer_role == self.current_player and not self.winner :
                self.computer_move()

                        
   
    def check_for_winner(self):        

        self.check_columns()
        self.check_rows()
        self.check_diagonals()
        self.check_tie()  
        
        if self.winner:
            self.declare_winner_callback(self.winner)        


    def check_rows(self):
        for row in self.board:
            
            if row.count(row[0]) == len(row) and row[0] != 0:
                self.winner = row[0]  
                break

    def check_columns(self):
        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0] [col]!= 0:
                self.winner = self.board[0][col]
                break

    def check_diagonals(self):
         if self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[1][1] != 0:
                self.winner = self.board[1][1]     

    def check_tie(self):
        if all([all(row) for row in self.board]) and self.winner is None:
         self.winner = "Deu Velha!"


    def switch_turn(self):
        self.current_player = self.player[1] if self.current_player == self.player[0] else self.player[0]   

    def is_cell_empty(self, row, col):
        return self.board[row][col] == 0      
   
       