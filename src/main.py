import customtkinter as ctk
from classes.login import LoginApp
from classes.register import RegisterApp
from classes.fixture import FixtureApp
from classes.ranking import RankingApp
from classes.predict import PredictApp
from classes.admin_page import AdminPageApp
import subprocess
from classes.index import IndexApp


class Main:
    def __init__(self):
        self.root = ctk.CTk()
        self.username = None
        self.show_login()

    def set_username(self, username):
        self.username = username

    def show_fixture(self, event=None):
        self.clear_window()
        self.fixture_app = FixtureApp(self.root, self.show_index)

    def show_ranking(self, event=None):
        self.clear_window()
        self.ranking_app = RankingApp(self.root, self.show_index)

    def show_predict(self, event=None):
        self.clear_window()
        if self.username:
            self.predict_app = PredictApp(self.root, self.show_index, self.username)
        else:
            self.show_login()
       
    def show_index(self):
        self.clear_window()
        self.index_app = IndexApp(self.root, self.show_fixture, self.show_ranking, self.show_predict)

    def show_login(self):
        self.clear_window()
        self.login_app = LoginApp(self.root, self.show_register, self.show_index, self.set_username, self.show_admin_page)

    def show_admin_page(self):
        self.clear_window()
        self.admin_app = AdminPageApp(self.root)

    def show_register(self):
        self.clear_window()
        self.register_app = RegisterApp(self.root, self.show_login, self.show_index, self.set_username, self.show_admin_page)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Iniciar la API en un proceso separado
    api_process = subprocess.Popen(["python", "src/Api/API.py"])

    # Iniciar la aplicación principal
    main_app = Main()
    main_app.start() 

    # Terminar el proceso de la API al cerrar la aplicación
    api_process.terminate()