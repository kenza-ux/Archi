import tkinter as tk
from tkinter import messagebox, ttk
from Hexagonal.appli.Mirror_v4 import MirrorApp
from Hexagonal.appli.Dictio import Dictionnaire
from Hexagonal.appli.TimeDay import TimeOfDay
from Hexagonal.appli.TextUtilities import TextUtilities

class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palindrome Verification Application")
        self.geometry("400x300")

        # Initialisation de Dictio et TimeDay pour MirrorApp
        self.dictionary = Dictionnaire()
        self.time = TimeOfDay()

        # Langue par défaut définie à "fr"
        self.lang = "fr"

        # Initialisation de MirrorApp avec les dépendances
        self.mirror_app = MirrorApp(self.dictionary, self.time, self.lang)

        # Initialisation des éléments d'interface utilisateur
        self.create_language_choice_widgets()

    def create_language_choice_widgets(self):
        self.clear_widgets()
        # Choix de la langue
        self.lang_var = tk.StringVar(value=self.lang)
        ttk.Label(self, text="Choose the language:").pack()
        ttk.Radiobutton(self, text="Français", variable=self.lang_var, value="fr").pack()
        ttk.Radiobutton(self, text="English", variable=self.lang_var, value="en").pack()
        ttk.Button(self, text="Confirm", command=self.confirm_language).pack(pady=10)

    def confirm_language(self):
        self.lang = self.lang_var.get()
        self.mirror_app.lang = self.lang  # Mise à jour de la langue dans MirrorApp

        # Déterminez la période de la journée
        current_hour = self.time.get_current_hour()
        period = self.time.get_time_of_day(current_hour)

        # Récupérez le message de bienvenue approprié
        welcome_message = self.dictionary.get_greeting(self.lang, period)
        messagebox.showinfo("Language", welcome_message)

        self.create_palindrome_check_widgets()

    def create_palindrome_check_widgets(self):
        self.clear_widgets()
        if self.lang == "en" :
            ttk.Label(self, text="Enter a word:").pack(pady=10)
            self.text_entry = ttk.Entry(self)
            self.text_entry.pack(pady=5)
            ttk.Button(self, text="Check", command=self.check_palindrome).pack(pady=10)

            self.result_label = ttk.Label(self, text="")
            self.result_label.pack(pady=10)

            ttk.Button(self, text="Try Again", command=self.create_language_choice_widgets).pack(pady=10)

        elif self.lang == "fr":
            ttk.Label(self, text="Entrez du texte:").pack(pady=10)
            self.text_entry = ttk.Entry(self)
            self.text_entry.pack(pady=5)
            ttk.Button(self, text="vérifier", command=self.check_palindrome).pack(pady=10)

            self.result_label = ttk.Label(self, text="")
            self.result_label.pack(pady=10)

            ttk.Button(self, text="essayer encore une fois", command=self.create_language_choice_widgets).pack(pady=10)

    def check_palindrome(self):
        text = self.text_entry.get()
        lang = self.lang
        if lang == "fr" :
            if TextUtilities.is_palindrome(text):
                response = f"'{text}' Bien dit ."
            else:
                mirrored_text = TextUtilities.mirror_text(text)
                response = f" En mirroir : '{mirrored_text}'"
            self.result_label['text'] = response
        elif lang == "en" :
            if TextUtilities.is_palindrome(text):
                response = f"'{text}' Well said! ."
            else:
                mirrored_text = TextUtilities.mirror_text(text)
                response = f"'{text}'  Mirrored: '{mirrored_text}'"
            self.result_label['text'] = response

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()