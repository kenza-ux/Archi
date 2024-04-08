
from Hexagonal.appli.Dictio import Dictionnaire
from Hexagonal.appli.TimeDay import TimeOfDay
class MirrorApp:
    def __init__(self, lang="fr"):
        self.lang = lang.lower()
        self.current_hour = TimeOfDay.get_current_hour()
        self.dictionary = Dictionnaire()
        self.time = TimeOfDay()

    def get_greeting(self):
        period = self.time.get_time_of_day(self.current_hour)
        return self.dictionary.get_greeting(self.lang, period)


    def mirror_text(self, text):
        return text[::-1]

    def is_palindrome(self, text):
        cleaned_text = text.lower().replace(" ", "")
        return cleaned_text == cleaned_text[::-1]

    def get_farewell(self):
        period = self.time.get_time_of_day(self.current_hour)
        return self.dictionary.get_farewell(self.lang, period)

    def get_input_prompt(self, key):
        return self.dictionary.get_input_message(self.lang, key)

    def run(self):
        print(self.get_greeting())
        input_prompt = self.get_input_prompt("entrer")

        while True:
            user_input = input(input_prompt).lower()
            if user_input == 'exit':
                break

            if self.is_palindrome(user_input):
                print(self.get_input_prompt("reponse"))
            else:
                mirrored_text = self.mirror_text(user_input)
                print(self.get_input_prompt("m"), mirrored_text)

        print(self.get_farewell())

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"
    app = MirrorApp(lang_choice)
    app.run()
