import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):
    def test_init(self):
        lothar = Weapon("Axe", 20, 0.56)
        self.assertEqual("Axe", lothar.type)
        self.assertEqual(20, lothar.damage)
        self.assertEqual(0.56, lothar.critical_percent)

    def test_critical_hit_true(self):
        warglaive = Weapon("Sword", 11, 1)
        self.assertTrue(warglaive.critical_hit())

    def test_critical_hit_false(self):
        another_warglaive = Weapon("Sword (again)", 10, 0)
        self.assertFalse(another_warglaive.critical_hit())

    def test_bad_crit(self):
        with self.assertRaises(ValueError):
            Weapon("Axe", 20, 100)

if __name__ == '__main__':
    unittest.main()
