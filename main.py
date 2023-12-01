import tkinter as tk
import customtkinter
from Game import Game
from BoardGUI import BoardGUI

def main():
    root = tk.Tk()
    board = BoardGUI(root)    
    root.mainloop()

if __name__ == "__main__":
    main()    