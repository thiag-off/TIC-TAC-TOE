import tkinter as tk
from tkinter import messagebox
from Game import Game
class BoardGUI:
    def __init__(self,master, opponent_type, player_symbol):
        
        self.master = master
        self.opponent_type = opponent_type
        self.player_symbol = player_symbol
        self.master.title("TIC TAC TOE")
        self.draw_board()
        self.game = Game(self.update_button, self.declare_winner, self.player_symbol, self.opponent_type)

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", height = 6, width = 20,
                 command= lambda row=i, col=j: self.game.handle_click(row, col) )
                button.grid(row=i, column=j)       
    
   


    def update_button(self, row, col, symbol):
        button = self.master.grid_slaves(row=row, column=col)[0]
        button.config(text = symbol) 
    
    
    def  declare_winner(self, winner):
        if winner == "Deu Velha!":
        
            message = winner
        
        else:
            message = f"{winner}  venceu." 
        
        answer = messagebox.askyesno("Fim de Jogo", message + " Quer jogar novamente?")

        if answer:
            self.draw_board()
            self.game.set_game()
        else:
            self.master.quit()                           
                       
        