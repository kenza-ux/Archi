import unittest
from Hexagonal.TextUtilities import TextUtilities


class TestConsoleMode(unittest.TestCase):
    def test_is_palindrome(self):
        """Teste que la méthode is_palindrome renvoie True pour un palindrome."""
        self.assertTrue(TextUtilities.is_palindrome("radar"))
        self.assertFalse(TextUtilities.is_palindrome("openai"))


    def test_mirror_text(self):
        """Teste que la méthode mirror_text renvoie le miroir d'un texte."""
        self.assertEqual(TextUtilities.mirror_text("abc"), "cba")
        self.assertEqual(TextUtilities.mirror_text("OpenAI"), "IAnepO")
        self.assertEqual(TextUtilities.mirror_text(""), "")


if __name__ == "__main__":
    unittest.main()
