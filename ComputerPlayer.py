

import math

class ComputerPlayer:
    def __init__(self,player):
        self.player = player
        
   
    def find_best_move(self,board):
        
        best_eval = -math.inf
        
        best_move = None
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = self.player[0]
                    eval = self.mini_max(board, False)
                    board[row][col] = 0
                    if eval > best_eval:                        
                        best_eval = eval
                        best_move = [row, col]
        
        return best_move

    def mini_max(self,board, isMaximizing):
        eval = self.check_for_winner(board)
        if eval is not None:
            return eval

        elif isMaximizing:
            max_eval = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = self.player[0]
                        #print(board)
                        eval = self.mini_max(board, False)
                        board[row][col] = 0
                        max_eval = max(eval, max_eval)
            return max_eval

        else :
            min_eval = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = self.player[1]
                        #print(board)
                        eval = self.mini_max(board, True)
                        board[row][col] = 0
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


    def random_point(board):
        
        rand1 = random.randint(0,2)
        rand2 = random.randint(0,2)

        if board[0].count(0) > 0 or board[1].count(0) > 0 or board[2].count(0) > 0:
            if board[rand1][rand2] == 0 :
                return rand1, rand2
                   
            else:                
                self.random_point(board)        