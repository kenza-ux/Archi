class TextUtilities:
    @staticmethod
    def mirror_text(text):
        if not isinstance(text, str):
            raise TypeError("Le texte doit être une chaîne de caractères.")
        return text[::-1]

    @staticmethod
    def is_palindrome(text):
        if not isinstance(text, str):
            raise TypeError("Le texte doit être une chaîne de caractères.")
        cleaned_text = text.lower().replace(" ", "")
        return cleaned_text == cleaned_text[::-1]