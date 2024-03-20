import datetime

class MirrorApp:
    def __init__(self, lang="fr"):
        self.lang = lang.lower()
        self.current_hour = datetime.datetime.now().hour

    def get_greeting(self):
        greetings = {
            "en": {
                "morning": "Good morning",
                "afternoon": "Good afternoon",
                "evening": "Good evening",
                "night": "Good night",
            },
            "fr": {
                "morning": "Bonjour",
                "afternoon": "Bon après-midi",
                "evening": "Bonsoir",
                "night": "Bonne nuit",
            }
        }
        period = self._get_time_of_day()
        return greetings[self.lang][period]

    def _get_time_of_day(self):
        if 5 <= self.current_hour < 12:
            return "morning"
        elif 12 <= self.current_hour < 18:
            return "afternoon"
        elif 18 <= self.current_hour < 22:
            return "evening"
        else:
            return "night"

    def mirror_text(self, text):
        return text[::-1]

    def is_palindrome(self, text):
        cleaned_text = text.lower().replace(" ", "")
        return cleaned_text == cleaned_text[::-1]

    def get_farewell(self):
        farewells = {
            "en": {
                "morning": "Goodbye, see you soon",
                "afternoon": "Goodbye, see you later",
                "evening": "Goodbye, see you tonight",
                "night": "Goodbye, see you tomorrow",
            },
            "fr": {
                "morning": "Au revoir, à bientôt",
                "afternoon": "Au revoir, à tout à l'heure",
                "evening": "Au revoir, à ce soir",
                "night": "Bonne nuit, à demain",
            }
        }
        period = self._get_time_of_day()
        return farewells[self.lang][period]

    def print_message(self, message):
        print(message)

    def run(self):
        self.print_message(self.get_greeting())

        input_prompt = "Entrez du texte (ou 'exit' pour quitter): " if self.lang == "fr" else "Type here (or 'exit' to quit): "
        while True:
            user_input = input(input_prompt).lower()

            if user_input == 'exit':
                break

            if self.is_palindrome(user_input):
                self.print_message("Bien dit !" if self.lang == "fr" else "Well said!")
            else:
                mirrored_text = self.mirror_text(user_input)
                self.print_message(f"En miroir : {mirrored_text}" if self.lang == "fr" else f"Mirrored: {mirrored_text}")

        self.print_message(self.get_farewell())

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"
    app = MirrorApp(lang_choice)
    app.run()
