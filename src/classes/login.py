from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp:
    def __init__(self, root, switch_to_register, switch_to_index, set_username):
        self.root = root
        self.switch_to_register = switch_to_register
        self.switch_to_index = switch_to_index
        self.set_username = set_username
        self.root.title("Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.create_login_fields()

    def create_login_fields(self):
        fields_frame = ctk.CTkFrame(master=self.frame)
        fields_frame.pack(pady=12, padx=10)

        welcome_label = ctk.CTkLabel(master=fields_frame, text='Welcome to the penca of the copa america 2024', font=("Arial", 18))
        welcome_label.grid(row=0, columnspan=2, pady=12, padx=10)

        username_icon = Image.open("Assets/Images/Icons/username.png")
        username_icon = username_icon.resize((20, 20), Image.LANCZOS)
        username_icon = ctk.CTkImage(username_icon, size=(20, 20))

        password_icon = Image.open("Assets/Images/Icons/password.png")
        password_icon = password_icon.resize((20, 20), Image.LANCZOS)
        password_icon = ctk.CTkImage(password_icon, size=(20, 20))

        username_label = ctk.CTkLabel(master=fields_frame, image=username_icon, text="")
        username_label.image = username_icon
        username_label.grid(row=1, column=0, padx=10, pady=5)

        self.user_entry = ctk.CTkEntry(master=fields_frame, placeholder_text="Username", width=300, height=40, corner_radius=10)
        self.user_entry.grid(row=1, column=1, padx=10, pady=5)

        password_label = ctk.CTkLabel(master=fields_frame, image=password_icon, text="")
        password_label.image = password_icon
        password_label.grid(row=2, column=0, padx=10, pady=5)

        self.user_pass = ctk.CTkEntry(master=fields_frame, placeholder_text="Password", show="*", width=300, height=40, corner_radius=10)
        self.user_pass.grid(row=2, column=1, padx=10, pady=5)

        self.login_button = ctk.CTkButton(master=fields_frame, text='Login', command=self.login, width=300, height=40, corner_radius=10)
        self.login_button.grid(row=3, columnspan=2, pady=12, padx=10)

        self.register_label = ctk.CTkLabel(master=fields_frame, text="Don't have an account? Register", text_color="white", cursor="hand2")
        self.register_label.grid(row=4, columnspan=2, pady=12, padx=10)
        self.register_label.bind("<Button-1>", lambda e: self.switch_to_register())

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo
        self.image_label.pack(pady=10)

    def login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()

        if not username or not password:
            tkmb.showerror("Error", "Please enter both username and password")
            return

        try:
            response = requests.post("http://localhost:5000/login", json={
                "Username": username,
                "Password": password
            })
            if response.status_code == 200:
                self.set_username(username)
                self.switch_to_index()
            elif response.status_code == 400:
                tkmb.showwarning(title='Login Failed', message='Missing username or password')
            elif response.status_code == 401 or  response.status_code == 404:
                tkmb.showwarning(title='Login Failed', message='Invalid username or password')
            else:
                tkmb.showerror("Error", "Login failed: " + response.json().get('error', 'Unknown error'))
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to login: {e}")