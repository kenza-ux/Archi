import tkinter as tk
from tkinter import messagebox, ttk
from Hexagonal.TextUtilities import TextUtilities


class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palindrome Verification Application")
        self.geometry("400x300")

        self.messages = {
            "fr": {
                "welcome": "Bienvenue",
                "is_palindrome": "est un palindrome.",
                "not_palindrome": "n'est pas un palindrome.",
                "choose_language": "Choisir la langue :",
                "enter_word": "Entrez un mot :",
                "check": "Vérifier",
                "try_again": "Nouvel essai"
            },
            "en": {
                "welcome": "Welcome",
                "is_palindrome": "is a palindrome.",
                "not_palindrome": "is not a palindrome.",
                "choose_language": "Choose the language:",
                "enter_word": "Enter a word:",
                "check": "Check",
                "try_again": "Try Again"
            }
        }

        self.lang = "fr"  # Default language
        self.create_language_choice_widgets()

    def create_language_choice_widgets(self):
        self.clear_widgets()

        # Language choice
        self.lang_var = tk.StringVar(value=self.lang)
        ttk.Label(self, text=self.messages[self.lang]["choose_language"]).pack()
        ttk.Radiobutton(self, text="Français", variable=self.lang_var, value="fr").pack()
        ttk.Radiobutton(self, text="English", variable=self.lang_var, value="en").pack()
        ttk.Button(self, text="Confirm", command=self.confirm_language).pack(pady=10)

    def confirm_language(self):
        self.lang = self.lang_var.get()
        messagebox.showinfo("Language", self.messages[self.lang]["welcome"])
        self.create_palindrome_check_widgets()

    def create_palindrome_check_widgets(self):
        self.clear_widgets()

        # Palindrome check area
        ttk.Label(self, text=self.messages[self.lang]["enter_word"]).pack(pady=10)
        self.text_entry = ttk.Entry(self)
        self.text_entry.pack(pady=5)
        ttk.Button(self, text=self.messages[self.lang]["check"], command=self.check_palindrome).pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        ttk.Button(self, text=self.messages[self.lang]["try_again"], command=self.create_language_choice_widgets).pack(
            pady=10)

    def check_palindrome(self):
        text = self.text_entry.get()
        if TextUtilities.is_palindrome(text):
            self.result_label['text'] = f"'{text}' {self.messages[self.lang]['is_palindrome']}"
        else:
            self.result_label['text'] = f"'{text}' {self.messages[self.lang]['not_palindrome']}"

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()
