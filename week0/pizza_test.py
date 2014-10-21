import unittest
import os
from copy import deepcopy
from pizza import *


class TestPizza(unittest.TestCase):
    def setUp(self):
        self.save_file = open('pizza_test.txt', 'w')
        self.files = []
        self.orders = {}

    def tearDown(self):
        self.save_file.close()
        os.remove('pizza_test.txt')

    def test_take_order_valid(self):
        self.assertTrue(take(['', 'John', 20], self.orders))
        self.assertTrue(take(['', 'Vankata', 180.93], self.orders))

    def test_take_order_invalid(self):
        self.assertFalse(take(['', '', ''], self.orders))

    def test_saving_and_loading(self):
        take(['', 'John', 20], self.orders)
        take(['', 'Vankata', 180.93], self.orders)

        old_orders = deepcopy(self.orders)
        save(self.orders, 'file_names_test.txt')

        take(['', 'Peter', 200], self.orders)
        take(['', 'Vankata', 0.18], self.orders)

        self.assertNotEqual(old_orders, self.orders)
        self.files = list('file_names_test.txt')
        self.orders = load(self.files, 0)
        self.assertEqual(old_orders, self.orders)

        print("SELF FILES - {0}".format(self.files))
        for each in self.files:
            if each != '':
                os.remove(each)

        os.remove('file_names_test.txt')


if __name__ == '__main__':
    unittest.main()
