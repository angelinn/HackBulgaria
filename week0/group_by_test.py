import unittest
from group_by import group_by


class GroupByTest(unittest.TestCase):
    def test_group_by(self):
        first_result = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEqual(first_result, group_by(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

        second_result = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
        self.assertEqual(second_result, group_by(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

        third_result = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEqual(third_result,
                         group_by(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))

if __name__ == '__main__':
    unittest.main()
