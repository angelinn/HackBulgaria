import unittest
from hero import Hero
from player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        hero = Hero('Peter', 100, 'Johnson')
        player = Player('Player Uno', hero, 0, 0)

        self.assertEqual('Player Uno', player.name)
        self.assertEqual(hero, player.entity)
        self.assertEqual(0, player.i)
        self.assertEqual(0, player.j)

if __name__ == '__main__':
    unittest.main()
