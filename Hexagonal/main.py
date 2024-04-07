from Mirror_v4 import MirrorApp
from Dictio import Dictionnaire
from TimeDay import TimeOfDay
from interface import GUIApp  # Assurez-vous que GUIApp est correctement importé

if __name__ == "__main__":
    interface_choice = input("Choose interface type (console/gui): ").lower()
    if interface_choice not in ["gui", "console"]:
        print("Invalid  choice. Defaulting to console.")
        lang_choice = "console"

    if interface_choice == "gui":
        app = GUIApp()
        app.mainloop()
    else:
        lang_choice = input("Choose a language (fr for French, en for English): ").lower()
        if lang_choice not in ["fr", "en"]:
            print("Invalid language choice. Defaulting to French.")
            lang_choice = "fr"

        dictionary = Dictionnaire()
        time = TimeOfDay()
        app = MirrorApp(dictionary, time, lang_choice)
        app.run()

