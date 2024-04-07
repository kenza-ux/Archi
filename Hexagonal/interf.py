from tkinter import Tk, messagebox, ttk
import tkinter as tk
from Mirror_v4 import MirrorApp
from Dictio import Dictionnaire
from TimeDay import TimeOfDay
from TextUtilities import TextUtilities


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

        ttk.Label(self, text="Choisissez la langue:").pack()  # French label
        ttk.Radiobutton(self, text="Français", variable=self.lang_var, value="fr").pack()
        ttk.Radiobutton(self, text="English", variable=self.lang_var, value="en").pack()
        ttk.Button(self, text="Confirmer", command=self.confirm_language).pack(pady=10)

    def confirm_language(self):
        self.lang = self.lang_var.get()
        self.mirror_app.lang = self.lang  # Update language in MirrorApp

        # Déterminez la période de la journée
        current_hour = self.time.get_current_hour()
        period = self.time.get_time_of_day(current_hour)

        # Récupérez le message de bienvenue approprié
        welcome_message = self.dictionary.get_greeting(self.lang, period)
        messagebox.showinfo("Language", welcome_message)

        self.create_palindrome_check_widgets()

    def create_palindrome_check_widgets(self):
        self.clear_widgets()

        # Retrieve input messages based on language
        label_text = self.dictionary.get_input_message(self.lang, "entrer")
        button_text = self.dictionary.get_input_message(self.lang, "v")  # Assuming "v" is the key for "Check"
        try_again_text = self.dictionary.get_input_message(self.lang, "essai")

        # Create widgets using retrieved messages
        ttk.Label(self, text=label_text).pack(pady=10)
        self.text_entry = ttk.Entry(self)
        self.text_entry.pack(pady=5)
        ttk.Button(self, text=button_text, command=self.check_palindrome).pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        ttk.Button(self, text=try_again_text, command=self.create_language_choice_widgets).pack(pady=10)

    def check_palindrome(self):
        text = self.text_entry.get()

        if TextUtilities.is_palindrome(text):
            response = self.dictionary.get_input_message(self.lang, "reponse")
            formatted_message = response
        else:
            mirrored_text = TextUtilities.mirror_text(text)
            response = self.dictionary.get_input_message(self.lang, "m")
            formatted_message = f"{response}: '{mirrored_text}'"

            # Update the result label
        self.result_label['text'] = formatted_message

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()