import unittest
import os
from copy import deepcopy
from pizza import *


class TestPizza(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza()
        self.nab_file = open(self.pizza.file_names, 'r+')
        self.nab_file.truncate()

    def tearDown(self):
        for each in self.nab_file.read().split('\n'):
            if each != '':
                os.remove(each)

        self.nab_file.truncate()
        self.nab_file.close()

    def test_take_order_valid(self):
        self.assertTrue(self.pizza.take(['', 'John', 20]))
        self.assertTrue(self.pizza.take(['', 'Vankata', 180.93]))

    def test_take_order_invalid(self):
        with self.assertRaises(ValueError):
            self.pizza.take(['', '', ''])

    def test_saving_and_loading(self):
        self.pizza.take(['', 'John', 20])
        self.pizza.take(['', 'Vankata', 180.93])

        old_orders = deepcopy(self.pizza.orders)
        self.pizza.save()

        self.pizza.take(['', 'Peter', 200])
        self.pizza.take(['', 'Vankata', 0.18])

        self.assertNotEqual(old_orders, self.pizza.orders)
        self.pizza.files = self.pizza.list()
        self.pizza.orders = self.pizza.load(0)
        self.pizza.orders = self.pizza.load(0)
        self.assertEqual(old_orders, self.pizza.orders)

    def test_load_before_using_list(self):
        self.assertFalse(self.pizza.load(10))

    def test_load_with_using_list_with_unsaved_order(self):
        self.pizza.take(['', 'John', 20])
        self.pizza.list()
        self.assertFalse(self.pizza.load(2))


if __name__ == '__main__':
    unittest.main()
