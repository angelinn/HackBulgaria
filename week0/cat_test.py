import unittest
import os
from cat import cat


class CatTest(unittest.TestCase):
    def test_with_valid_text_file(self):
        path = 'cat_test.txt'
        test_file = open(path, 'w')
        content = "Python is an awesome language!\nYou should try it."
        test_file.write(content)
        test_file.close()

        again = open(path, 'r')
        self.assertEqual(content, cat(again))
        os.remove(path)

    def test_with_invalid_text_file(self):
        with self.assertRaises(BaseException):
            test_file = None
            cat(test_file)

if __name__ == '__main__':
    unittest.main()
