import customtkinter
import tkinter as tk
from tkinter import messagebox
from game import Game


class BoardGUI:
    def __init__(self, master, opponent_type, player_symbol, setup_screen_callback):
        self.master = master
        self.master.title("TIC TAC TOE")
        self.master.geometry("650x500")
        self.opponent_type = opponent_type
        self.player_symbol = player_symbol

        self.setup_screen_callback = setup_screen_callback

        self.board = customtkinter.CTkFrame(master=self.master)
        self.board.pack(pady=20, padx=60, expand=True)

        self.draw_board()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.game = Game(
            self.update_button,
            self.declare_winner,
            self.player_symbol,
            self.opponent_type,
        )

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                button = customtkinter.CTkButton(
                    master=self.board,
                    text="",
                    font=("Terminal", 60),
                    height=120,
                    width=120,
                    border_width=2,
                    command=lambda row=i, col=j: self.game.handle_click(row, col),
                )
                button.grid(row=i, column=j, sticky="nsew", pady=12, padx=10)

    def update_button(self, row, col, symbol):
        button = self.board.grid_slaves(row=row, column=col)[0]
        button.configure(text=symbol)

    def declare_winner(self, winner):
        if winner == "tie":
            message = "Deu Velha!"

        else:
            message = f"{winner}  venceu."

        answer = messagebox.askyesno("Fim de Jogo", message + " Quer jogar novamente?")

        if answer:
            self.draw_board()
            self.game.set_game()
        else:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            self.setup_screen_callback()

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja abandonar o jogo?"):
            self.master.destroy()
