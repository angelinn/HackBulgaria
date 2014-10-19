import unittest
from anbn import is_an_bn


class AnBnTest(unittest.TestCase):
    def test_letters(self):
        self.assertTrue(is_an_bn(""))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertTrue(is_an_bn("aaaaabbbbb"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertFalse(is_an_bn("rado"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))

if __name__ == '__main__':
    unittest.main()
