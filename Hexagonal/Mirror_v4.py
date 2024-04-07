
from TextUtilities import TextUtilities

class MirrorApp:
    def __init__(self, dictionary, time, lang="fr"):
        self.lang = lang.lower()
        self.current_hour = time.get_current_hour()
        self.dictionary = dictionary
        self.time = time

    def get_greeting(self):
        period = self.time.get_time_of_day(self.current_hour)
        return self.dictionary.get_greeting(self.lang, period)

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

            if TextUtilities.is_palindrome(user_input):
                print(self.get_input_prompt("reponse"))
            else:
                mirrored_text = TextUtilities.mirror_text(user_input)
                print(self.get_input_prompt("m"), mirrored_text)

        print(self.get_farewell())
