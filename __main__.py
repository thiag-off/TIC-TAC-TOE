import customtkinter
from views import SetupScreen


def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    setup = SetupScreen(root)

    root.mainloop()


if __name__ == "__main__":
    main()
