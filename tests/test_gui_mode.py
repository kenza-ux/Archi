import unittest
import sys
sys.path.append('C:\\Users\\HP\\OneDrive\\Documents\\archi\\Archi_grp_E\\Hexagonal')
from Hexagonal.interface import GUIApp
from unittest.mock import patch

class TestGUIApp(unittest.TestCase):
    def setUp(self):
        """Initialise l'application GUI pour chaque test."""
        self.app = GUIApp()
        self.app.update()  # Force l'actualisation de la fenêtre

    def tearDown(self):
        """Détruit l'application GUI après chaque test."""
        self.app.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_language_selection(self, mock_showinfo):
        """Teste si la sélection de la langue affiche la boîte de dialogue correcte."""
        self.app.lang_var.set("en")
        self.app.confirm_language()
        mock_showinfo.assert_called_with("Language", "Welcome")

    def test_palindrome_check_true(self):
        """Teste la vérification de palindrome pour un cas où le texte est un palindrome."""
        self.app.lang_var.set("en")  # Assurez-vous que le test se déroule en anglais
        self.app.confirm_language()  # Mise à jour des widgets pour refléter le choix de la langue
        self.app.text_entry.insert(0, "radar")
        self.app.check_palindrome()
        self.assertEqual(self.app.result_label['text'], "'radar' is a palindrome.")

    def test_palindrome_check_false(self):
        """Teste la vérification de palindrome pour un cas où le texte n'est pas un palindrome."""
        self.app.lang_var.set("fr")  # Test en français
        self.app.confirm_language()
        self.app.text_entry.insert(0, "python")
        self.app.check_palindrome()
        self.assertEqual(self.app.result_label['text'], "'python' n'est pas un palindrome.")

    # Ici, vous pouvez ajouter d'autres tests pour couvrir plus de fonctionnalités et de cas.

if __name__ == "__main__":
    unittest.main()
