import customtkinter as ctk
from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb


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

        self.champion_label = ctk.CTkLabel(master=self.frame, text="Which country will win the tornament?", cursor="hand2")
        self.champion_label.pack(pady=12, padx=10)
        self.champion_prediction_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Winner")
        self.champion_prediction_entry.pack(pady=12, padx=10)

        self.second_label = ctk.CTkLabel(master=self.frame, text="And the second place?", cursor="hand2")
        self.second_label.pack(pady=12, padx=10)
        self.second_prediction_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Runner-up")
        self.second_prediction_entry.pack(pady=12, padx=10)

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

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Aquí puedes agregar la lógica para registrar un nuevo usuario
        tkmb.showinfo("Register", f"User {username} registered successfully!")
