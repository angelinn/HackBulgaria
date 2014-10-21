import unittest
import os
from sum_numbers import sum_numbers


class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.numbers_file = open('numbers_test.txt', 'w')

    def tearDown(self):
        self.numbers_file.close()
        os.remove('numbers_test.txt')

    def test_is_sum_correct(self):
        self.numbers_file.write("10 20 30 40 50 60 70 80 90")
        self.numbers_file.flush()

        self.numbers_file = open('numbers_test.txt', 'r')
        self.assertEqual(450, sum_numbers(self.numbers_file))

if __name__ == '__main__':
    unittest.main()
