from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class IndexApp:
    def __init__(self, root, show_fixture, show_ranking, show_predict):
        self.root = root
        self.show_fixture = show_fixture
        self.show_ranking = show_ranking
        self.show_predict = show_predict

        self.root.title("Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        ctk.CTkLabel(self.root, text="Welcome to the fuckin penca bro").pack()

        # Crear un frame para contener los botones
        self.button_frame = ctk.CTkFrame(master=self.root)
        self.button_frame.pack(pady=20, padx=40, fill='both', expand=True)

        # Crear botones grandes y cuadrados
        self.create_button("Fixture", self.button_frame)
        self.create_button("Ranking", self.button_frame)
        self.create_button("Predict", self.button_frame)


    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def create_button(self, text, parent_frame):
        button_size = 350  # Tamaño del botón para hacerlo grande y cuadrado
        button = ctk.CTkButton(master=parent_frame, text=text, width=button_size, height=button_size)
        button.pack(pady=20, padx=20, side=ctk.LEFT, expand=True)

        if text == "Fixture":
            button.bind("<Button-1>", self.show_fixture)
        elif text == "Ranking":
            button.bind("<Button-1>", self.show_ranking)
        else:
            button.bind("<Button-1>", self.show_predict)

        

       