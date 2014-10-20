import unittest
from goldbach import goldbach


class GoldbachTest(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual([(2, 2)], goldbach(4))
        self.assertEqual([(3, 3)], goldbach(6))
        self.assertEqual([(3, 5)], goldbach(8))
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))

    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):
            goldbach(0)


if __name__ == '__main__':
    unittest.main()
