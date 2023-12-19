import customtkinter
import tkinter
import tkinter.messagebox
from controllers import GameCreator


class SetupScreen:
    def __init__(self, master):
        self.master = master
        self.create_screen()

    def create_screen(self):
        self.master.geometry("650x500")
        self.master.title("MENU - TIC TAC TOE")

        # Main-Frame
        self.frame = customtkinter.CTkFrame(master=self.master)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Menu-Title
        self.label = customtkinter.CTkLabel(
            master=self.frame, text="Menu", font=("Montserrat Bold", 30)
        )
        self.label.pack(pady=12, padx=10)

        # Frame_2
        self.frame_2 = customtkinter.CTkFrame(master=self.frame)
        self.frame_2.pack(pady=12, padx=10)

        # Radio-Button-FRAME
        self.radiobutton_frame = customtkinter.CTkFrame(master=self.frame_2)
        self.radiobutton_frame.grid(sticky="nsew")
        self.radiobutton_frame.pack(pady=12, padx=10)

        self.radio_var = tkinter.IntVar(value=0)

        # Play-With-Subtitle
        self.label_radio_group = customtkinter.CTkLabel(
            master=self.radiobutton_frame, text="Play with: "
        )
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky=""
        )

        # Radio-Button-1
        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame,
            variable=self.radio_var,
            value=0,
            text="Friend",
            command=lambda: self.optionmenu.configure(state="disabled"),
        )
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # Radio-Button-2
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame,
            variable=self.radio_var,
            value=1,
            text="Computer",
            command=lambda: self.optionmenu.configure(state="normal"),
        )
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # Play-As-Text
        self.label_optionmenu = customtkinter.CTkLabel(
            master=self.frame, text="Play as: ", font=("Montserrat", 24)
        )
        self.label_optionmenu.pack(pady=12, padx=10)

        # Option-Meno
        self.optionmenu = customtkinter.CTkOptionMenu(
            master=self.frame, values=["X", "O"], state="disabled"
        )
        self.optionmenu.pack(pady=12, padx=10)

        # Start-Button
        self.button_1 = customtkinter.CTkButton(
            master=self.frame,
            text="Start",
            font=("Montserrat", 18),
            command=lambda: self.start_game(self.master),
        )
        self.button_1.pack(pady=12, padx=10)

    def start_game(self, master):
        computer_player_enabled = False if self.radio_var.get() == 0 else True
        player_symbol = self.optionmenu.get()

        for widget in self.master.winfo_children():
            widget.pack_forget()

        game_creator = GameCreator(
            self.master, self.create_screen, player_symbol, computer_player_enabled
        )
