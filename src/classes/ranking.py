from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RankingApp:
    def __init__(self, root, show_index, username):
        self.root = root
        self.show_index = show_index
        self.username = username

        self.root.title("Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry(
            "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        ctk.CTkLabel(self.root, text="Ranking bro").pack()

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='Ranking')
        self.label.pack(pady=12, padx=10)

        self.back_button = ctk.CTkButton(
            master=self.frame, text="Back to Index", command=self.show_index)
        self.back_button.pack(pady=12, padx=10)
        self.display_ranking_table()

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def fetch_ranking(self):
        url = "http://localhost:5000/ranking"
        response = requests.get(url)
        if response.status_code == 200:
            ranking = response.json()
            return ranking
        return None

    def load_flag_image(self, country_id):
        url = f"http://localhost:5000/country/id?id={country_id}"
        response = requests.get(url)
        if response.status_code == 200:
            country_name = response.json()
            flag_path = f"Assets/Images/Flags/Flag_of_{country_name}.png"
            if os.path.exists(flag_path):
                flag_image = Image.open(flag_path)
                flag_image = flag_image.resize((30, 20), Image.LANCZOS)
                return ctk.CTkImage(light_image=flag_image, size=(30, 20))
            else:
                print(f"Bandera no encontrada para: {country_name}")
                return None
        else:
            print(f"Error al obtener el nombre del país para ID: {country_id}")
            return None

    def display_ranking_table(self):
        ranking_data = self.fetch_ranking()

        # Create a frame to hold the table and center it
        table_frame = ctk.CTkFrame(master=self.frame)
        table_frame.pack(pady=40, padx=40, anchor='center')
        
        # Header
        ctk.CTkLabel(table_frame, text="Rank", anchor='center', width=20).grid(row=0, column=0, padx=20, pady=10, sticky='ew')
        ctk.CTkLabel(table_frame, text="Username", anchor='center', width=20).grid(row=0, column=1, padx=20, pady=10, sticky='ew')
        ctk.CTkLabel(table_frame, text="Points", anchor='center', width=20).grid(row=0, column=2, padx=20, pady=10, sticky='ew')
        ctk.CTkLabel(table_frame, text="Champion", anchor='center', width=20).grid(row=0, column=3, padx=20, pady=10, sticky='ew')
        ctk.CTkLabel(table_frame, text="Sub Champion", anchor='center', width=20).grid(row=0, column=4, padx=20, pady=10, sticky='ew')

        # Data
        for index, entry in enumerate(ranking_data, start=1):
           
            username = entry["Username"]
            total_points = entry["Total Points"]
            champion = self.load_flag_image(entry["Champion"])
            sub_champion = self.load_flag_image(entry["Sub Champion"])
            
            if username == self.username:
                bg_color = "blue"
            else:
                bg_color = "#2b2b2b"       

            ctk.CTkLabel(table_frame, text=f"{index}", anchor='center', width=20, bg_color=bg_color).grid(row=index, column=0, padx=10, pady=10, sticky='ew')
            ctk.CTkLabel(table_frame, text=username, anchor='center', width=40, bg_color= bg_color).grid(row=index, column=1, padx=10, pady=10, sticky='ew')
            ctk.CTkLabel(table_frame, text=f"{total_points}", anchor='center', width=40, bg_color= bg_color).grid(row=index, column=2, padx=10, pady=10, sticky='ew')
            
            # Images cant be None because the user is already registered, so we don't need to check that
            ctk.CTkLabel(table_frame, image=champion,text="", anchor='center', width=40, bg_color= bg_color).grid(row=index, column=3, padx=10, pady=10, sticky='ew')
            ctk.CTkLabel(table_frame, image=sub_champion,text="", anchor='center', width=40,bg_color= bg_color).grid(row=index, column=4, padx=10, pady=10, sticky='ew')

        
