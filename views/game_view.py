import customtkinter
from tkinter import messagebox


class GameView:
    def __init__(self, master, setup_screen_callback):
        self.master = master
        self.master.title("TIC TAC TOE")
        self.master.geometry("650x500")

        self.setup_screen_callback = setup_screen_callback

        self.board = customtkinter.CTkFrame(master=self.master)
        self.board.pack(pady=20, padx=60, expand=True)

        self.draw_board()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.game_manager: object

    def set_manager(self, manager: object):
        self.game_manager = manager

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
                    command=lambda row=i, col=j: self.game_manager.handle_click(
                        row, col
                    ),
                )
                button.grid(row=i, column=j, sticky="nsew", pady=12, padx=10)

    def update_button(self):
        move = self.game_manager.get_last_move_made()
        button = self.board.grid_slaves(row=move[0], column=move[1])[0]
        button.configure(text=move[2])

    def declare_winner(self):
        winner = self.game_manager.get_winner()

        if winner == "tie":
            message = "Deu Velha!"

        else:
            message = f"{winner}  venceu."

        answer = messagebox.askyesno("Fim de Jogo", message + " Quer jogar novamente?")

        if answer:
            self.draw_board()
            self.game_manager.set_game()
        else:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            self.setup_screen_callback()

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja abandonar o jogo?"):
            self.master.destroy()
