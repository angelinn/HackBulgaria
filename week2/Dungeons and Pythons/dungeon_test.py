import unittest
import os
from dungeon import *


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.map_str = 'S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S'
        splitted = self.map_str.split('\n')
        self.ready_map = []

        for each in splitted:
            self.ready_map.append(list(each))

        dungeon_file = open('test_dungeon.txt', 'w')
        dungeon_file.write(self.map_str)
        dungeon_file.close()

        self.cool_dungeon = Dungeon('test_dungeon.txt')

    def tearDown(self):
        os.remove('test_dungeon.txt')

    def test_init_if_map_is_correct(self):
        print("first foo")
        self.assertEqual(self.ready_map, self.cool_dungeon.map_list)
        print(self.cool_dungeon.map_list)

    def test_spawn_with_valid_entity(self):
        print("second foo")
        self.assertTrue(self.cool_dungeon.spawn('Player Uno', Hero('John', 100, 'Kingslayer')))
        print(self.cool_dungeon.map_list)

    def test_spawn_with_two_entities(self):
        print("third foo")
        self.assertTrue(self.cool_dungeon.spawn('Player Tres', Hero('John', 100, 'Kingslayer')))
        self.assertTrue(self.cool_dungeon.spawn('Player Dos', Orc('Pete', 100, 3)))
        print('\n')
        #print("THIS SHOULD BE DIFFERENT ->")
        #self.cool_dungeon.print_map()
        print(self.cool_dungeon.map_list)

    def test_spawn_with_same_names(self):
        print("forth foo")
        with self.assertRaises(ValueError):
            self.cool_dungeon.spawn('Player Quatro', Hero('John', 100, 'Kingslayer'))
            self.cool_dungeon.spawn('Player Quatro', Orc('Pete', 100, 3))
        print(self.cool_dungeon.map_list)

if __name__ == '__main__':
    unittest.main()
