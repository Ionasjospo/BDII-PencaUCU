from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests
import datetime

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

        headers = ["Date", "Home team", "Away team"]

        for col, header in enumerate(headers):
            label = ctk.CTkLabel(master=table_frame, text=header, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

        if group == "A":
            data = self.matches(group)
        elif group == "B":
            data =  self.matches(group)
        else:
            data =  self.matches(group)     
        
        
        formatted_data = [
            [datetime.datetime.strptime(match['Date'], "%a, %d %b %Y %H:%M:%S %Z").strftime("%d/%m/%Y %H:%M:%S"), 
            match['Home team'], 
            match['Away team']] 
            for match in data]

        if formatted_data is not None:
            for row, entry in enumerate(formatted_data, start=1):
                for col, item in enumerate(entry):
                    label = ctk.CTkLabel(master=table_frame, text=item)
                    label.grid(row=row, column=col, padx=5, pady=5)
    

    def matches(self, group):
        try:
            response = requests.post("http://localhost:5000/matches", json={
                "group": group,
                "group": group,
                })
            if response.status_code == 200:
                matches = response.json()
                return matches
            else:
                tkmb.showerror("Error", "Failed to load matches")
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to load matches: {e}")

    