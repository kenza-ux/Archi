class Dictionnaire:
    def __init__(self):
        self._greetings = {
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

        self._farewells = {
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

        self._inputs_run = {
            "fr": {
                "entrer": "Entrez du texte (ou 'exit' pour quitter): ",
                "m": "En mirroir",
                "reponse": "Bien dit !"
             },
            "en": {
                "entrer": "Type here (or 'exit' to quit): ",
                "m": "Mirrored",
                "reponse": "Well said!"
            }
        }

    def get_greeting(self, lang, period):
        return self._greetings.get(lang, {}).get(period, "")

    def get_farewell(self, lang, period):
        return self._farewells.get(lang, {}).get(period, "")

    def get_input_message(self, lang, key):
        return self._inputs_run.get(lang, {}).get(key, "")

# Exemple d'utilisation :
d = Dictionnaire()
print(d.get_greeting("en", "morning"))  # Output: Good morning
print(d.get_farewell("fr", "evening"))  # Output: Au revoir, à ce soir
print(d.get_input_message("en", "entrer"))  # Output: Type here (or 'exit' to quit):
