import tkinter as tk
import customtkinter
from Game import Game

def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()    