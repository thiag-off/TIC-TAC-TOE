import customtkinter
import tkinter
import tkinter.messagebox
from BoardGUI import BoardGUI

class SetupScreen:
    def __init__(self, master):          
        
        self.master = master
        self.master.geometry("850x500")
        self.master.title("MENU - TIC TAC TOE")
        self.frame = customtkinter.CTkFrame(master = self.master)
        self.frame.pack(pady = 20, padx = 60, fill="both", expand=True)
        self.label = customtkinter.CTkLabel(master= self.frame, text="Menu", font=("Montserrat", 24))
        self.label.pack(pady = 12, padx = 10)
        

        self.frame_2 = customtkinter.CTkFrame(master= self.frame)
        
        self.radiobutton_frame = customtkinter.CTkFrame(master=self.frame_2)        
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        self.radio_var = tkinter.IntVar(value=0)
        
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Play with: ")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
         value=0, text= "Friend", command= lambda: self.optionmenu.configure(state = "disabled"))
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,
         text= "Computer", command= lambda: self.optionmenu.configure(state = "normal"))
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        
        self.frame_2.pack(pady = 12, padx = 10)
        self.radiobutton_frame.pack(pady = 12, padx = 10)
        
        self.label_optionmenu = customtkinter.CTkLabel(master= self.frame, text="Play as: " , font=("Montserrat", 24))
        self.label_optionmenu.pack(pady = 12, padx = 10)
        self.optionmenu = customtkinter.CTkOptionMenu(master= self.frame, values=["X", "O"], state="disabled")        
        self.optionmenu.pack(pady=12, padx = 10)
        
        self.button_1 = customtkinter.CTkButton(master = self.frame, text="Start", font=("Montserrat", 18),
         command = lambda: self.start_game(self.master) )
        self.button_1.pack(pady = 12, padx = 10)
    
    def start_game(self, master):
        opponent_type = "Friend" if self.radio_var.get() == 0 else "Computer"
        player_symbol = self.optionmenu.get()

       

        self.master.withdraw()
        root = tkinter.Tk()
        board = BoardGUI(root, opponent_type, player_symbol)