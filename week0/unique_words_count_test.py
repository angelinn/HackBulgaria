import unittest
from unique_words_count import unique_words_count


class UniqueWordsCountTest(unittest.TestCase):
    def test_unique_words(self):
        unique_words = ['false', 'true', 'equals', 'pro', 'noob']
        first_count = 5

        repetetive_words = ['false', 'true', 'equals', 'pro', 'true']
        second_count = 4

        self.assertEqual(first_count, unique_words_count(unique_words))
        self.assertEqual(second_count, unique_words_count(repetetive_words))

if __name__ == '__main__':
    unittest.main()
