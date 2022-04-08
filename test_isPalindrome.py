from unittest import TestCase
import unittest
from isPalindrome import *


class IsItPalindrome(unittest.TestCase):
    # Here we test if we are giving a string and correct type of response which is in fact a palindrome
    def test_correct_type_input(self):
        phrase = "madam"
        answer = is_palindrome(phrase)
        self.assertEqual(phrase, answer)

    # Here we are aiming for a typeError so instead of giving it a str, we give it an int
    def test_error(self):
        phrase = 6
        answer = is_palindrome(phrase)
        with self.assertRaises(TypeError):
            self.assertEqual(phrase, answer)


if __name__ == '__main__':
    unittest.main()
