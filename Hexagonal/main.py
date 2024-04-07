from Mirror_v4 import MirrorApp

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"
    app = MirrorApp(lang_choice)
    app.run()