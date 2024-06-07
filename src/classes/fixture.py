from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests
import datetime
import os

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

        button_frame = ctk.CTkFrame(master=self.root)
        button_frame.pack(pady=12, padx=10)

        self.back_button = ctk.CTkButton(master=button_frame, text="Back to Index", command=self.show_index)
        self.back_button.pack(side='left', padx=10)

        self.frame = ctk.CTkScrollableFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.create_table("A", "Group A")
        self.create_table("B", "Group B")
        self.create_table("C", "Group C")

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)
        self.photo = ctk.CTkImage(light_image=image, size=(200, 100))
        self.image_label = ctk.CTkLabel(master=self.root, image=self.photo, text="")
        self.image_label.pack(pady=10)

    def create_table(self, group, group_name):
        matches = self.fetch_matches(group)
        if matches:
            matches.sort(key=lambda x: datetime.datetime.strptime(x['Date'].replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S"))

            group_label = ctk.CTkLabel(master=self.frame, text=group_name, font=("Arial", 16, "bold"))
            group_label.pack(pady=10)

            for match in matches:
                match_datetime = datetime.datetime.strptime(match['Date'].replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S")
                formatted_datetime = match_datetime.strftime("%d-%m - %H:%M")

                match_frame = ctk.CTkFrame(master=self.frame)
                match_frame.pack(pady=12, padx=10, fill='x')

                match_inner_frame = ctk.CTkFrame(master=match_frame)
                match_inner_frame.pack(anchor='center')

                time_label = ctk.CTkLabel(master=match_inner_frame, text=formatted_datetime, font=("Arial", 12))
                time_label.pack(side='left', padx=5)

                home_flag = self.load_flag_image(match['Home team'])
                home_flag_label = ctk.CTkLabel(master=match_inner_frame, image=home_flag, text="")
                home_flag_label.pack(side='left', padx=5)

                home_team_label = ctk.CTkLabel(master=match_inner_frame, text=match['Home team'])
                home_team_label.pack(side='left')

                vs_label = ctk.CTkLabel(master=match_inner_frame, text=" Vs ")
                vs_label.pack(side='left')

                away_team_label = ctk.CTkLabel(master=match_inner_frame, text=match['Away team'])
                away_team_label.pack(side='left')

                away_flag = self.load_flag_image(match['Away team'])
                away_flag_label = ctk.CTkLabel(master=match_inner_frame, image=away_flag, text="")
                away_flag_label.pack(side='left', padx=5)

    def load_flag_image(self, country_name):
        flag_path = f"Assets/Images/Flags/Flag_of_{country_name}.png"
        if os.path.exists(flag_path):
            flag_image = Image.open(flag_path)
            flag_image = flag_image.resize((30, 20), Image.LANCZOS)
            return ctk.CTkImage(light_image=flag_image, size=(30, 20))
        else:
            print(f"Flag not founded to : {country_name}")
            return None

    def fetch_matches(self, group):
        try:
            response = requests.get(f"http://localhost:5000/matches?group={group}")
            if response.status_code == 200:
                return response.json()
            else:
                tkmb.showerror("Error", "Failed to load matches")
                return []
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to load matches: {e}")
            return []
