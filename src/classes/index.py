from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class IndexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penca UCU")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.load_image("Assets/Images/ucu_white_logo.png")

        ctk.CTkLabel(self.root, text="Welcome to the fuckin penca bro").pack()


    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)
        username = self.user_entry.get()
        password = self.user_pass.get()

        if not username or not password:
            tkmb.showerror("Error", "Please enter both username and password")
            return

        new_window = ctk.CTkToplevel(self.root)
        new_window.title("New Window")
        new_window.geometry("350x150")

        try:
            response = requests.post("http://localhost:5000/login", json={
                "Username": username,
                "Password": password
            })
            if response.status_code == 200:
                tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
                # new_window = ctk.CTkToplevel(self.root)
                # new_window.title("New Window")
                # new_window.geometry("350x150")
                # ctk.CTkLabel(new_window, text="Welcome to the Penca UCU!").pack()
            elif response.status_code == 400:
                tkmb.showwarning(title='Login Failed', message='Missing username or password')
            elif response.status_code == 401 or  response.status_code == 404:
                tkmb.showwarning(title='Login Failed', message='Invalid username or password')
            else:
                tkmb.showerror("Error", "Login failed: " + response.json().get('error', 'Unknown error'))
        except requests.RequestException as e:
            tkmb.showerror("Error", f"Failed to login: {e}")