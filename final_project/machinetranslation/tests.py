import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_translation(self):
        # Test translation 
        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = french_to_english(french_text)
        self.assertEqual(translation, expected_translation)

class TranslationTestss(unittest.TestCase):
    def test_translation(self):
        # Test translation 
        eng_text = "Hello"
        expected_translation = "Bonjour"
        translation = english_to_french(eng_text)
        self.assertEqual(translation, expected_translation)

if __name__ == '__main__':
    unittest.main()

