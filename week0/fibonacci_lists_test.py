import unittest
from fibonacci_lists import fibonacci_lists


class FibonacciListsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1], fibonacci_lists([1], [2], 1))

    def test_two(self):
        self.assertEqual([2], fibonacci_lists([1], [2], 2))

    def test_more(self):
        self.assertEqual([1, 2, 1, 3], fibonacci_lists([1, 2], [1, 3], 3))
        self.assertEqual([1, 2, 3, 1, 2, 3], fibonacci_lists([], [1, 2, 3], 4))
        self.assertEqual([], fibonacci_lists([], [], 100))

if __name__ == '__main__':
    unittest.main()
