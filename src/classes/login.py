from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp:
    def __init__(self, root, switch_to_register):
        self.root = root
        self.switch_to_register = switch_to_register
        self.root.title("Penca UCU")
        self.root.geometry("500x500")

        self.load_image("Assets/Images/ucu_white_logo.png")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='Welcome to the penca of the copa america 2024')
        self.label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.frame, text='Login', command=self.login)
        self.login_button.pack(pady=12, padx=10)

        # self.checkbox = ctk.CTkCheckBox(master=self.frame, text='Remember Me')
        # self.checkbox.pack(pady=12, padx=10)

        # Cambiar fg a text_color
        self.register_label = ctk.CTkLabel(master=self.frame, text="Don't have an account? Register", text_color="blue", cursor="hand2")
        self.register_label.pack(pady=12, padx=10)
        self.register_label.bind("<Button-1>", lambda e: self.switch_to_register())

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 150), Image.LANCZOS)  # Resize the image
        photo = ImageTk.PhotoImage(image)
        self.image_label = ctk.CTkLabel(master=self.root, image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def login(self):
        username = "admin"
        password = "admin"
        new_window = ctk.CTkToplevel(self.root)
        new_window.title("New Window")
        new_window.geometry("350x150")

        if self.user_entry.get() == username and self.user_pass.get() == password:
            tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
            ctk.CTkLabel(new_window, text="GeeksforGeeks is best for learning ANYTHING !!").pack()
        elif self.user_entry.get() == username and self.user_pass.get() != password:
            tkmb.showwarning(title='Wrong password', message='Please check your password')
        elif self.user_entry.get() != username and self.user_pass.get() == password:
            tkmb.showwarning(title='Wrong username', message='Please check your username')
        else:
            tkmb.showerror(title="Login Failed", message="Invalid Username and password")
