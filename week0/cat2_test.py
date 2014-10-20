import unittest
import os
from cat2 import read_multiple_content


class Cat2Test(unittest.TestCase):
    def setUp(self):
        path_one = 'cat1.txt'
        self.first_file = open(path_one, 'w')
        self.first_content = 'mega pro voltron uber'
        self.first_file.write(self.first_content)
        self.first_file.flush()
        self.first_file = open(path_one, 'r')

        path_two = 'cat2.txt'
        self.second_file = open(path_two, 'w')
        self.second_content = 'another mega cool line'
        self.second_file.write(self.second_content)
        self.second_file.flush()
        self.second_file = open(path_two, 'r')

    def tearDown(self):
        os.remove('cat1.txt')
        os.remove('cat2.txt')

    def test_one_file(self):
        self.assertEqual(self.first_content, read_multiple_content(self.first_file))

    def test_multiple_files(self):
        self.assertEqual(self.first_content + '\n' + self.second_content,
                         read_multiple_content(self.first_file, self.second_file))

if __name__ == '__main__':
    unittest.main()
