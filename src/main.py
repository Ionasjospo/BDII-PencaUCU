import customtkinter as ctk
from classes.login import LoginApp
from classes.register import RegisterApp

class Main:
    def __init__(self):
        self.root = ctk.CTk()
        self.show_login()

    def show_login(self):
        self.clear_window()
        self.login_app = LoginApp(self.root, self.show_register)

    def show_register(self):
        self.clear_window()
        self.register_app = RegisterApp(self.root, self.show_login)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    main = Main()
    main.start()
