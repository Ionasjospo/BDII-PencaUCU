import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as tkmb
import requests


class RegisterApp:
    def __init__(self, root, switch_to_login, switch_to_index):
        self.root = root
        self.switch_to_login = switch_to_login
        self.switch_to_index = switch_to_index
        self.root.title("Register to Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        self.frame = ctk.CTkScrollableFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='Register to Penca UCU')
        self.label.pack(pady=12, padx=10)

        self.document_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Document")
        self.document_entry.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.name_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Name")
        self.name_entry.pack(pady=12, padx=10)

        self.surname_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Surname")
        self.surname_entry.pack(pady=12, padx=10)

        self.email_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Email")
        self.email_entry.pack(pady=12, padx=10)

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


        # Ver aca si command= self.register es true cambiar a login app
        self.register_button = ctk.CTkButton(master=self.frame, text='Register', command=self.register)
        self.register_button.pack(pady=12, padx=10)
        

        self.login_label = ctk.CTkLabel(master=self.frame, text="Already have an account? Login", cursor="hand2")
        self.login_label.pack(pady=12, padx=10)
        self.login_label.bind("<Button-1>", lambda e: self.switch_to_login())

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
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
        document = self.document_entry.get()
        username = self.username_entry.get()
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        champion_prediction = self.champion_prediction_entry.get()
        second_prediction = self.second_prediction_entry.get()

        if not all([document, username, name, surname, email, password, champion_prediction, second_prediction]):
            tkmb.showerror("Error", "Please fill in all fields")
            return

        try:
            response = requests.post("http://localhost:5000/register", json={
                "Document": document,
                "Username": username,
                "Name": name,
                "Surname": surname,
                "Email": email,
                "Password": password,
                "Champion_Prediction": champion_prediction,
                "Second_Prediction": second_prediction
            })
            if response.status_code == 200:
                tkmb.showinfo("Success", "User registered successfully!")
                self.switch_to_index()
                return True
            else:
                tkmb.showerror("Error", f"Failed to register: {response.json().get('error', 'Unknown error')}")
                return False
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to register: {e}")
