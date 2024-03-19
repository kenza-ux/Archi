import datetime

class MirrorApp:
    def __init__(self, lang="fr"):
        self.lang = lang.lower()
        self.current_hour = datetime.datetime.now().hour

    def get_greeting(self):
        if self.lang == "en":
            if 5 <= self.current_hour < 12:
                return "Good morning"
            elif 12 <= self.current_hour < 18:
                return "Good afternoon"
            elif 18 <= self.current_hour < 22:
                return "Good evening"
            else:
                return "Good night"
        else:  # Default to French
            if 5 <= self.current_hour < 12:
                return "Bonjour"
            elif 12 <= self.current_hour < 18:
                return "Bon après-midi"
            elif 18 <= self.current_hour < 22:
                return "Bonsoir"
            else:
                return "Bonne nuit"

    def mirror_text(self, text):
        return text[::-1]

    def is_palindrome(self, text):
        text = text.lower()
        return text == text[::-1]

    def get_farewell(self):
        if self.lang == "en":
            if 5 <= self.current_hour < 12:
                return "Goodbye, see you soon"
            elif 12 <= self.current_hour < 18:
                return "Goodbye, see you later"
            elif 18 <= self.current_hour < 22:
                return "Goodbye, see you tonight"
            else:
                return "Goodbye, see you tomorrow"
        else:  # Default to French
            if 5 <= self.current_hour < 12:
                return "Au revoir, à bientôt"
            elif 12 <= self.current_hour < 18:
                return "Au revoir, à tout à l'heure"
            elif 18 <= self.current_hour < 22:
                return "Au revoir, à ce soir"
            else:
                return "Bonne nuit, à demain"

    def run(self):
        print(self.get_greeting())

        while True:
            user_input = input("Entrez du texte (ou 'exit' pour quitter): ")

            if user_input.lower() == 'exit':
                break

            mirrored_text = self.mirror_text(user_input)
            print(f"En miroir : {mirrored_text}")

            if self.is_palindrome(user_input):
                print("Bien dit !")

        print(self.get_farewell())

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"
    app = MirrorApp(lang_choice)
    app.run()
