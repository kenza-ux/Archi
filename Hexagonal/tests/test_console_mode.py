import unittest

import sys
sys.path.append('/Hexagonal')
from unittest.mock import call, patch

from Hexagonal.appli.Mirror_v4 import MirrorApp
from Hexagonal.appli.Dictio import Dictionnaire
from Hexagonal.appli.TimeDay import TimeOfDay

class TestConsoleMode(unittest.TestCase):
    @patch('InputHandler.get_input')
    @patch('TextUtilities.is_palindrome')
    def test_run_palindrome(self, mock_is_palindrome, mock_get_input):  # Remove mock_mirror_text
        mock_is_palindrome.return_value = True
        mock_get_input.return_value = "kayak"

        dictionary = Dictionnaire()
        time = TimeOfDay()
        app = MirrorApp(dictionary, time)
        app.run()

        mock_get_input.assert_called_once_with("entrer")
        mock_is_palindrome.assert_called_once_with("kayak")

        # Removed calls related to mirror_text
        dictionary.display_message.assert_has_calls([
            call(app.get_greeting()),
            call(app.get_input_prompt("reponse")),
            call(app.get_farewell())
        ])

if __name__ == "__main__":
    unittest.main()