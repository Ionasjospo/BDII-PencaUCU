import customtkinter as ctk
from classes.login import LoginApp
from classes.register import RegisterApp
import subprocess

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
    # Iniciar la API en un proceso separado
    api_process = subprocess.Popen(["python", "src/classes/API.py"])

    # Iniciar la aplicación principal
    main_app = Main()
    main_app.start()

    # Terminar el proceso de la API al cerrar la aplicación
    api_process.terminate()
