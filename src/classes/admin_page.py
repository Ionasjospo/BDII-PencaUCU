from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import requests
import datetime
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AdminPageApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Penca UCU - Admin Page")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.matches = {}
        self.load_image("Assets/Images/ucu_white_logo.png")

        ctk.CTkLabel(self.root, text="Upload the final football match results", font=("Arial", 18)).pack(pady=10)

        button_frame = ctk.CTkFrame(master=self.root)
        button_frame.pack(pady=12, padx=10)

        self.submit_button = ctk.CTkButton(master=button_frame, text="Submit", command=self.submit_matches)
        self.submit_button.pack(side='left', padx=10)

        self.frame = ctk.CTkScrollableFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.get_matches_to_update_score()

       
    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((200, 100), Image.LANCZOS)  # Resize the image
        photo = ctk.CTkImage(image, size=(250, 150))
        self.image_label = ctk.CTkLabel(master=self.root, image=photo, text="")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=10)

    def get_matches_to_update_score(self):
        response = requests.get('http://localhost:5000/matches?predictable=false&username=admin')
        if response.status_code == 200:
            matches = response.json()
            self.create_match_inputs(matches)
        else:
            tkmb.showerror("Error", "Failed to fetch matches")

    def create_match_inputs(self, matches):
        matches.sort(key=lambda x: datetime.datetime.strptime(x['Date'].replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S"))

        grouped_matches = {}
        for match in matches:
            date_str = datetime.datetime.strptime(match['Date'].replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S").strftime("%Y-%m-%d")
            if date_str not in grouped_matches:
                grouped_matches[date_str] = []
            grouped_matches[date_str].append(match)

        for date_str, matches_on_date in grouped_matches.items():
            date_label = ctk.CTkLabel(master=self.frame, text=date_str, font=("Arial", 16, "bold"))
            date_label.pack(pady=10)

            for match in matches_on_date:
                match_datetime = datetime.datetime.strptime(match['Date'].replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S")
                formatted_date = match_datetime.strftime("%m-%d")
                formatted_time = match_datetime.strftime("%H:%M")

                match_frame = ctk.CTkFrame(master=self.frame)
                match_frame.pack(pady=12, padx=10, fill='x')

                match_inner_frame = ctk.CTkFrame(master=match_frame)
                match_inner_frame.pack(anchor='center')

                time_label = ctk.CTkLabel(master=match_inner_frame, text=formatted_time, font=("Arial", 12))
                time_label.pack(side='left', padx=5)

                home_flag = self.load_flag_image(match['Home team'])
                home_flag_label = ctk.CTkLabel(master=match_inner_frame, image=home_flag, text="")
                home_flag_label.pack(side='left', padx=5)

                match_label = ctk.CTkLabel(master=match_inner_frame, text=f"{match['Home team']} [")
                match_label.pack(side='left')

                home_score_entry = ctk.CTkEntry(master=match_inner_frame, width=50)
                home_score_entry.pack(side='left', padx=5)
                if 'home_score' in match and match['home_score'] is not None:
                    home_score_entry.insert(0, str(match['home_score']))

                match_label = ctk.CTkLabel(master=match_inner_frame, text=f"] Vs [")
                match_label.pack(side='left')

                away_score_entry = ctk.CTkEntry(master=match_inner_frame, width=50)
                away_score_entry.pack(side='left', padx=5)
                if 'away_score' in match and match['away_score'] is not None:
                    away_score_entry.insert(0, str(match['away_score']))

                match_label = ctk.CTkLabel(master=match_inner_frame, text=f"] {match['Away team']}")
                match_label.pack(side='left')

                away_flag = self.load_flag_image(match['Away team'])
                away_flag_label = ctk.CTkLabel(master=match_inner_frame, image=away_flag, text="")
                away_flag_label.pack(side='left', padx=5)

                id_home_country = match.get('id_home_country', None)
                id_away_country = match.get('id_away_country', None)
                self.matches[match['id_match']] = (home_score_entry, away_score_entry, id_home_country, id_away_country)

    def load_flag_image(self, country_name):
        flag_path = f"Assets/Images/Flags/Flag_of_{country_name}.png"
        if os.path.exists(flag_path):
            flag_image = Image.open(flag_path)
            flag_image = flag_image.resize((30, 20), Image.LANCZOS)
            return ctk.CTkImage(light_image=flag_image, size=(30, 20))
        else:
            print(f"Bandera no encontrada para: {country_name}")
            return None

    def submit_matches(self):
        matches_updated_data = {
            "matches_updated": []
        }

        for match_id, (home_score_entry, away_score_entry, id_home_country, id_away_country) in self.matches.items():
            try:
                home_score = int(home_score_entry.get())
                away_score = int(away_score_entry.get())
                if home_score >= 0 and away_score >= 0 and id_home_country is not None and id_away_country is not None:
                    matches_updated_data["matches_updated"].append({
                        "id_match": match_id,
                        "home_score": home_score,
                        "away_score": away_score
                    })
            except ValueError:
                # Ignore entries that are not valid integers
                continue

        if matches_updated_data:
            response = requests.post('http://localhost:5000/submit_matches', json=matches_updated_data)
            if response.status_code == 200:
                tkmb.showinfo("Success", "Predictions submitted successfully")
            else:
                tkmb.showerror("Error", "Failed to submit predictions")
        else:
            tkmb.showwarning("Warning", "No valid predictions to submit")
