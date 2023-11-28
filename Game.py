import tkinter as tk
from tkinter import messagebox
import random 
from ComputerPlayer import ComputerPlayer


class Game:
    def __init__(self,master):
        self.master = master
        master.title("TIC TAC TOE")
       
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = ["X", "O"]
        self.computer_role = self.player[0]
        self.computer_player = ComputerPlayer(self.player)
        self.create_game()
        
        

    def computer_move(self):
        move = self.computer_player.find_best_move([row[:] for row in self.board])
        self.handle_click(move[0],move[1])
        
     # [["X","O",0],["O","O",0],[0,"X","X"]]  

        
   
    def create_game(self):

        self.current_player = self.player[0]

        for i in range(3):
            for j in range(3):
                self.button = tk.Button(self.master, text="", height = 6, width = 20, command= lambda row=i, col=j: self.handle_click(row, col) )
                self.button.grid(row=i, column=j)         
        
        if self.computer_role == self.current_player:
            self.computer_move()        

    def handle_click(self, row, col):
        

        if self.board[row][col] == 0:
            if self.current_player == self.player[0]:
                self.board[row][col] = self.player[0]
                self.current_player = self.player[1]                
                
            else:
                self.board[row][col] = self.player[1]
                self.current_player = self.player[0]
            
            self.button = self.master.grid_slaves(row=row, column=col)[0]
            self.button.config(text = self.board[row][col])                 
                       
            self.check_for_winner()
            
            if self.computer_role == self.current_player:
                self.computer_move()

    def check_for_winner(self):
        winner = None
        
        for row in self.board:
            
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]  
                break
                            

        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0] [col]!= 0:
                winner = self.board[0][col]
                break
                

        if self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[1][1] != 0:
                winner = self.board[1][1]  
            
              
        if all([all(row) for row in self.board]) and winner is None:
         winner = "Deu Velha!"
        if winner:
            self.declare_winner(winner)     

    def  declare_winner(self, winner):
        if winner == "Deu Velha!":
            message = winner
        else:
            message = f"{winner}  venceu." 
        
        answer = messagebox.askyesno("Fim de Jogo", message + " Quer jogar novamente?")

        if answer:
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            for i in range(3):
                for j in range(3):
                    button = self.master.grid_slaves(row=i, column=j)[0]
                    button.config(text="")
                    
            self.current_player = self.player[0]
        
        else:
            self.master.quit()       




            
    







        


 

        