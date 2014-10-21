import unittest
from generate_numbers import generate_numbers
import os


class TestGenerateNumbers(unittest.TestCase):
    def setUp(self):
        self.wfile = open('numbers.txt', 'w')

    def tearDown(self):
        self.wfile.close()
        os.remove('numbers.txt')

    def test_generating_numbers(self):
        generate_numbers(100, self.wfile)
        self.wfile.flush()

        self.wfile = open('numbers.txt', 'r')
        content = self.wfile.read().split(' ')

        self.assertEqual(100, len(content) - 1)

if __name__ == '__main__':
    unittest.main()
