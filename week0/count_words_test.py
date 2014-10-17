import unittest
from count_words import count_words


class CountWordsTest(unittest.TestCase):
    def test_unique_words(self):
        correct = {
            'apple': 1,
            'orange': 1,
            'pineapple': 1
            }

        test_words = ['apple', 'orange', 'pineapple']

        self.assertEqual(correct, count_words(test_words))

    def test_repetitive_words(self):
        correct = {
            'apple': 4,
            'strawberry': 2,
            'plum': 3
        }

        test_words = ['apple', 'apple', 'plum', 'strawberry',
                      'apple', 'strawberry', 'plum', 'apple', 'plum']

        self.assertEqual(correct, count_words(test_words))


if __name__ == '__main__':
    unittest.main()
