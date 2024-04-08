from Hexagonal.appli.Mirror_v4 import MirrorApp
from Hexagonal.appli.Dictio import Dictionnaire
from Hexagonal.appli.TimeDay import TimeOfDay

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"

    dictionary = Dictionnaire()
    time = TimeOfDay()
    app = MirrorApp(dictionary, time, lang_choice)
    app.run()
