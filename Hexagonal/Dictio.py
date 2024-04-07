# Constantes à modifier/ améliorer plus facielement sans toucher directement au corps de la classe
# pour une
GREETINGS = {
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

FAREWELLS = {
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

INPUTS_RUN = {
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
class Dictionnaire:
    def __init__(self):
        self._greetings = GREETINGS
        self._farewells = FAREWELLS
        self._inputs_run = INPUTS_RUN

    def get_greeting(self, lang, period):
        return self._greetings.get(lang, {}).get(period, "Language or period not supported")

    def get_farewell(self, lang, period):
        return self._farewells.get(lang, {}).get(period, "Language or period not supported")

    def get_input_message(self, lang, key):
        return self._inputs_run.get(lang, {}).get(key, "Language or period not supported")

    def get_error_message(self, lang, error_key):
            errors = {
                "fr": {
                    "type_error": "Erreur de type.",
                    "general_error": "Une erreur s'est produite.",
                },
                "en": {
                    "type_error": "Type error.",
                    "general_error": "An error occurred.",
                }
            }
            return errors.get(lang, {}).get(error_key, errors[lang]["general_error"])