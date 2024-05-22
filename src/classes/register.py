import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as tkmb
import requests


class RegisterApp:
    def __init__(self, root, switch_to_login):
        self.root = root
        self.switch_to_login = switch_to_login
        self.root.title("Register to Penca UCU")
        self.root.geometry("750x750")

        self.load_image("Assets/Images/ucu_white_logo.png")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='Register to Penca UCU')
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.document_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Document")
        self.document_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.champion_label = ctk.CTkLabel(master=self.frame, text="Which country will win the tournament?")
        self.champion_label.pack(pady=12, padx=10)
        self.champion_prediction_entry = ctk.CTkComboBox(master=self.frame)
        self.champion_prediction_entry.pack(pady=12, padx=10)

        self.second_label = ctk.CTkLabel(master=self.frame, text="And the second place?")
        self.second_label.pack(pady=12, padx=10)
        self.second_prediction_entry = ctk.CTkComboBox(master=self.frame)
        self.second_prediction_entry.pack(pady=12, padx=10)

        self.load_countries()

        self.register_button = ctk.CTkButton(master=self.frame, text='Register', command=self.register)
        self.register_button.pack(pady=12, padx=10)

        self.login_label = ctk.CTkLabel(master=self.frame, text="Already have an account? Login", cursor="hand2")
        self.login_label.pack(pady=12, padx=10)
        self.login_label.bind("<Button-1>", lambda e: self.switch_to_login())

        # self.scrollbar = ctk.CTkScrollbar(master=self.frame)
        # self.scrollbar.pack(side='right', fill='y')

        # self.frame_text = ctk.CTkTextbox(master=self.frame, yscrollcommand=self.scrollbar.set)
        # self.frame_text.pack(pady=12, padx=10, fill='both', expand=True)

        # self.scrollbar.configure(command=self.frame_text.yview)


    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ImageTk.PhotoImage(image)
        self.image_label = ctk.CTkLabel(master=self.root, image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def load_countries(self):
        try:
            response = requests.get("http://localhost:5000/countries")
            if response.status_code == 200:
                countries = response.json()
                country_names = list(countries.keys())
                self.champion_prediction_entry.configure(values=country_names)
                self.second_prediction_entry.configure(values=country_names)
            else:
                tkmb.showerror("Error", "Failed to load countries")
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to load countries: {e}")

    def register(self):
        username = self.username_entry.get()
        document = self.document_entry.get()
        password = self.password_entry.get()
        champion_prediction = self.champion_prediction_entry.get()
        second_prediction = self.second_prediction_entry.get()

        if not username or not document or not password or not champion_prediction or not second_prediction:
            tkmb.showerror("Error", "Please fill in all fields")
            return

        try:
            response = requests.post("http://localhost:5000/register", json={
                "Username": username,
                "Document": document,
                "Password": password,
                "Champion_Prediction": champion_prediction,
                "Second_Prediction": second_prediction
            })
            if response.status_code == 200:
                tkmb.showinfo("Success", "User registered successfully!")
            else:
                tkmb.showerror("Error", f"Failed to register: {response.json().get('error', 'Unknown error')}")
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to register: {e}")
