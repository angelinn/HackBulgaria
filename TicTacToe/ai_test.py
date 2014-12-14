import unittest
from ai import AI
from game import Game


class AITest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.AI = AI(self.game.UI.BOARD, self.game.winning_routes)

    def test_init(self):
        self.assertEqual(self.AI.BOARD, self.game.UI.BOARD)
        self.assertEqual(self.AI.winning_routes, self.game.winning_routes)

    def test_get_correct_position_when_two_places_marked_vertical(self):
        BOARD = [['X', ' ', ' '],
                 ['X', ' ', ' '],
                 [' ', ' ', ' ']]

        self.AI.BOARD = BOARD
        self.assertEqual((2, 0), self.AI.get_best_position())

    def test_get_correct_position_when_two_places_marked_horizontal(self):
        BOARD = [[' ', ' ', ' '],
                 ['X', ' ', 'X'],
                 [' ', ' ', ' ']]

        self.AI.BOARD = BOARD
        self.assertEqual((1, 1), self.AI.get_best_position())

    def test_get_correct_position_when_two_places_marked_diagonal(self):
        BOARD = [[' ', ' ', 'X'],
                 [' ', 'X', ' '],
                 [' ', ' ', ' ']]

        self.AI.BOARD = BOARD
        self.assertEqual((2, 0), self.AI.get_best_position())

    def test_when_only_one_place_is_marked(self):
        BOARD = [[' ', 'X', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        self.AI.BOARD = BOARD
        self.AI.attack()

        for line in self.AI.BOARD:
            for place in line:
                if place == 'O':
                    self.assertTrue(True)
                    return

        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
