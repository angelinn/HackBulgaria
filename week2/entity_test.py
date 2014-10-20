import unittest
from entity import Entity


class TestHero(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("Bron", 100)

    def test_hero_init(self):
        self.assertEqual(100, self.entity.health)
        self.assertEqual("Bron", self.entity.name)

    def test_get_health(self):
        self.assertEqual(100, self.entity.health)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_is_alive_not(self):
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_get_damage(self):
        self.entity.take_damage(60)
        self.assertEqual(40, self.entity.get_health())

    def test_get_damage_to_negative_health(self):
        self.entity.take_damage(150)
        self.assertEqual(0, self.entity.get_health())

    def test_get_healing_dead(self):
        self.entity.take_damage(100)
        self.assertFalse(self.entity.get_healing(200))

    def test_get_healing_more_than_health(self):
        self.entity.get_healing(250)
        self.assertEqual(100, self.entity.get_health())

    def test_get_healing_successful(self):
        self.entity.health = 20
        self.assertTrue(self.entity.get_healing(80))

if __name__ == '__main__':
    unittest.main()
