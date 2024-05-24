from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FixtureApp:
    def __init__(self, root, show_index):
        self.root = root
        self.show_index = show_index

        self.root.title("Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        ctk.CTkLabel(self.root, text="Fixture bro").pack()

        
        self.frame = ctk.CTkScrollableFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='Group A')
        self.label.pack(pady=12, padx=10)

        self.create_table("A")

        self.label = ctk.CTkLabel(master=self.frame, text='Group B')
        self.label.pack(pady=12, padx=10)

        self.create_table("B")

        self.label = ctk.CTkLabel(master=self.frame, text='Group C')
        self.label.pack(pady=12, padx=10)
        self.create_table("C")



        self.back_button = ctk.CTkButton(master=self.frame, text="Back to Index", command=self.show_index)
        self.back_button.pack(pady=12, padx=10)


    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def create_table(self, group):
        table_frame = ctk.CTkFrame(master=self.frame)
        table_frame.pack(pady=12, padx=10)

        headers = ["Home team", "Away team", "Date"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(master=table_frame, text=header, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

        data = []

        if group == "A":
            data = [
                ["Uruguay", "Argentina", "3/12/24 21:00"],
                ["Bolivia", "Brasil", "2/3/24 21:09"]
            ]
        elif group == "B":
            data = [
                ["Peru", "Chile", "3/12/24 21:00"],
                ["Paraguay", "Ecuador", "2/3/24 21:09"]
            ]
        else:
            data = [
                ["Venezuela", "Colombia", "3/12/24 21:00"],
                ["Qatar", "Australia", "2/3/24 21:09"]
            ]
        
        

        for row, entry in enumerate(data, start=1):
            for col, item in enumerate(entry):
                label = ctk.CTkLabel(master=table_frame, text=item)
                label.grid(row=row, column=col, padx=5, pady=5)
        

    