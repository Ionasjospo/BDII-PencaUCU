import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as tkmb
import requests
import re

class RegisterApp:
    def __init__(self, root, switch_to_login, switch_to_index, set_username):
        self.root = root
        self.switch_to_login = switch_to_login
        self.switch_to_index = switch_to_index
        self.set_username = set_username
        self.root.title("Register to Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        self.container_frame = ctk.CTkFrame(master=self.root)
        self.container_frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.frame = ctk.CTkFrame(master=self.container_frame, width=800)
        self.frame.pack(pady=20, padx=40)

        self.label = ctk.CTkLabel(master=self.frame, text='Register to Penca UCU', font=("Arial", 16, "bold"))
        self.label.grid(row=0, columnspan=4, pady=12)

        self.create_form_fields()
        self.load_countries()
        self.create_buttons()

    def create_form_fields(self):
        fields = [
            ("Document", 1, 0),
            ("First Name", 2, 0),
            ("Last Name", 3, 0),
            ("Email", 4, 0),
            ("Username", 1, 1),
            ("Password", 2, 1),
            ("Champion Prediction", 3, 1),
            ("Second Prediction", 4, 1)
        ]

        for field, row, col in fields:
            label = ctk.CTkLabel(master=self.frame, text=field)
            label.grid(row=row, column=col*2, pady=12, padx=10, sticky='e')

            if field == "Password":
                entry = ctk.CTkEntry(master=self.frame, placeholder_text=field, show="*")
            elif field in ["Champion Prediction", "Second Prediction"]:
                entry = ctk.CTkComboBox(master=self.frame)
                entry.set(field)
            else:
                entry = ctk.CTkEntry(master=self.frame, placeholder_text=field)

            entry.grid(row=row, column=col*2+1, pady=12, padx=10, sticky='w')
            setattr(self, f"{field.lower().replace(' ', '_')}_entry", entry)

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo
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

    def create_buttons(self):
        self.register_button = ctk.CTkButton(master=self.frame, text='Register', command=self.register)
        self.register_button.grid(row=5, columnspan=4, pady=12, padx=10)

        self.login_label = ctk.CTkLabel(master=self.frame, text="Already have an account? Login", cursor="hand2")
        self.login_label.grid(row=6, columnspan=4, pady=12, padx=10)
        self.login_label.bind("<Button-1>", lambda e: self.switch_to_login())

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def register(self):
        document = self.document_entry.get()
        username = self.username_entry.get()
        name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        champion_prediction = self.champion_prediction_entry.get()
        second_prediction = self.second_prediction_entry.get()

        if not all([document, username, name, last_name, email, password, champion_prediction, second_prediction]):
            tkmb.showerror("Error", "Please fill in all fields")
            return

        if not self.validate_email(email):
            tkmb.showerror("Error", "Invalid email format")
            return

        try:
            response = requests.post("http://localhost:5000/register", json={
                "Document": document,
                "Username": username,
                "Name": name,
                "Surname": last_name,
                "Email": email,
                "Password": password,
                "Champion_Prediction": champion_prediction,
                "Second_Prediction": second_prediction
            })
            if response.status_code == 200:
                tkmb.showinfo("Success", "User registered successfully!")
                self.set_username(username)
                self.switch_to_index()
                return True
            else:
                tkmb.showerror("Error", f"Failed to register: {response.json().get('error', 'Unknown error')}")
                return False
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to register: {e}")
