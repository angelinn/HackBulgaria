import unittest
import os
from concat_files import concat_files


class TestConcatFiles(unittest.TestCase):
    def setUp(self):
        self.file_one = open('test_one.txt', 'w')
        self.file_two = open('test_two.txt', 'w')

    def tearDown(self):
        self.file_one.close()
        self.file_two.close()

        os.remove('test_one.txt')
        os.remove('test_two.txt')

    def test_concatenation(self):
        uno = "Megatron is OP"
        dos = "But magneto moar."

        self.file_one.write(uno)
        self.file_two.write(dos)

        self.file_one = open('test_one.txt', 'r')
        self.file_two = open('test_two.txt', 'r')

        concat_files(self.file_one, self.file_two)

        megatron = open('MEGATRON', 'r')
        self.assertEqual('{0}\n{1}'.format(uno, dos),
                         megatron.read())

if __name__ == '__main__':
    unittest.main()
