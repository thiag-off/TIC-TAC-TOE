
import random
import math

class ComputerPlayer:
    def __init__(self,player,computer_symbol):
        self.player = player
        self.computer_symbol = computer_symbol

      
   
    def find_best_move(self, board):
        
        best_eval = self.best_eval_setup(self.computer_symbol)              

        possible_moves = self.get_random_possible_moves(board)

        for possible_move in possible_moves:
            
            board[possible_move[0]][possible_move[1]] = self.computer_symbol

            eval = self.mini_max(board, self.is_maximizing(self.next_player(self.computer_symbol))) 
            
            board[possible_move[0]][possible_move[1]] = 0

            if self.is_maximizing(self.computer_symbol):
                if eval > best_eval:                        
                        best_eval = eval
                        best_move = [possible_move[0], possible_move[1]]
            else:
                if eval < best_eval:                        
                        best_eval = eval
                        best_move = [possible_move[0], possible_move[1]]   
                    
        
        return best_move

    def mini_max(self,board, isMaximizing):

        eval = self.check_for_winner(board)
        if eval is not None:
            return eval

        elif isMaximizing:
            max_eval = -math.inf

            for possible_move in self.get_ordered_possible_moves(board):
                    board[possible_move[0]][possible_move[1]] = self.player[0]
                    eval = self.mini_max(board, False)
                    board[possible_move[0]][possible_move[1]] = 0
                    max_eval = max(eval, max_eval)
            return max_eval

        else :
            min_eval = math.inf
            for possible_move in self.get_ordered_possible_moves(board):
                    board[possible_move[0]][possible_move[1]] = self.player[1]
                    eval = self.mini_max(board, True)
                    board[possible_move[0]][possible_move[1]] = 0
                    min_eval = min(eval , min_eval)
            return min_eval
            
                  


    def check_for_winner(self, board):
        winner = None
        scores = {"tie" : 0, "X" : 1, "O" : -1}    
    
        for row in board:
            
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]  
                break
                            

        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] and board[0] [col]!= 0:
                winner = board[0][col]
                break
                

        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] != 0:
                winner = board[1][1]  

        if all([all(row) for row in board]) and winner is None:
            winner = "tie"
        
        if winner != None:
            return scores[winner]   


    def get_random_possible_moves(self, board:list ) -> list:  
        
        possible_moves = self.get_ordered_possible_moves(board)                   
                          
        random.shuffle(possible_moves)
                       
        return possible_moves

    def get_ordered_possible_moves(self, board:list) -> list:

        possible_moves = [(row , col) for row in range(3) for col in range(3) if board[row][col] == 0]                   

        return possible_moves      

    def is_maximizing(self, player:str) -> bool:

        return player == "X"

    def next_player(self, current_player:str) -> str:

        return {
            "X" : "O",
            "O" : "X"
        }[current_player]

    def best_eval_setup(self, player : str) -> int:  
        
        if self.is_maximizing(player):

            return -math.inf

        else:
            
            return math.inf               
