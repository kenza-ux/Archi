import unittest
from Hexagonal.TextUtilities import TextUtilities  # Assurez-vous que le chemin d'importation est correct

class TestConsoleMode(unittest.TestCase):
    def test_is_palindrome_true(self):
        """Teste que la méthode is_palindrome renvoie True pour un palindrome."""
        self.assertTrue(TextUtilities.is_palindrome("radar"))
        self.assertTrue(TextUtilities.is_palindrome("level"))
        self.assertTrue(TextUtilities.is_palindrome(""))

    def test_is_palindrome_false(self):
        """Teste que la méthode is_palindrome renvoie False pour un non-palindrome."""
        self.assertFalse(TextUtilities.is_palindrome("python"))
        self.assertFalse(TextUtilities.is_palindrome("openai"))

    def test_mirror_text(self):
        """Teste que la méthode mirror_text renvoie le miroir d'un texte."""
        self.assertEqual(TextUtilities.mirror_text("abc"), "cba")
        self.assertEqual(TextUtilities.mirror_text("OpenAI"), "IAnepO")
        self.assertEqual(TextUtilities.mirror_text(""), "")

    # Vous pouvez ajouter ici d'autres tests pour les différentes méthodes de TextUtilities

if __name__ == "__main__":
    unittest.main()
