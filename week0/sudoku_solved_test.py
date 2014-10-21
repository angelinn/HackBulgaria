import unittest
from sudoku_solved import *


class TestSudokuSolved(unittest.TestCase):
    def setUp(self):
        self.sudoku_correct = [
                              [4, 5, 2, 3, 8, 9, 7, 1, 6],
                              [3, 8, 7, 4, 6, 1, 2, 9, 5],
                              [6, 1, 9, 2, 5, 7, 3, 4, 8],
                              [9, 3, 5, 1, 2, 6, 8, 7, 4],
                              [7, 6, 4, 9, 3, 8, 5, 2, 1],
                              [1, 2, 8, 5, 7, 4, 6, 3, 9],
                              [5, 7, 1, 8, 9, 2, 4, 6, 3],
                              [8, 9, 6, 7, 4, 3, 1, 5, 2],
                              [2, 4, 3, 6, 1, 5, 9, 8, 7]]

        self.sudoku_incorrect = [
                                [4, 5, 2, 4, 5, 6, 7, 8, 9],
                                [3, 8, 7, 4, 5, 6, 7, 8, 9],
                                [6, 1, 9, 4, 5, 6, 7, 8, 9],
                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [1, 2, 3, 4, 6, 6, 7, 8, 9],
                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    def test_check_line_true(self):
        for i in range(9):
            self.assertTrue(check_line(self.sudoku_correct[i]))

    def test_check_line_false(self):
        for i in range(9):
            if check_line(self.sudoku_incorrect[i]) is False:
                self.assertFalse(check_line(self.sudoku_incorrect[i]))
                return

        self.assertFalse(True)

    def test_check_col_true(self):
        for i in range(9):
            self.assertTrue(check_column(self.sudoku_correct, i))

    def test_check_col_false(self):
        for i in range(9):
            if check_column(self.sudoku_incorrect, i) is False:
                self.assertFalse(check_column(self.sudoku_incorrect, i))
                return

        self.assertFalse(True)

    def test_little_square_true(self):
        self.assertTrue(check_little_square(self.sudoku_correct, 3, 0))

    def test_little_square_false(self):
        self.assertFalse(check_little_square(self.sudoku_incorrect, 3, 3))

    def test_true(self):
        self.assertTrue(sudoku_solved(self.sudoku_correct))

    def test_false(self):
        self.assertFalse(sudoku_solved(self.sudoku_incorrect))

if __name__ == '__main__':
    unittest.main()
