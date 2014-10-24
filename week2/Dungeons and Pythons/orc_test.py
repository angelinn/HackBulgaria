import unittest
from orc import Orc
from weapon import Weapon


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.thrall = Orc("Thrall", 100, 1.2)

    def test_orc_init(self):
        self.assertEqual(100, self.thrall.health)
        self.assertEqual("Thrall", self.thrall.name)
        self.assertEqual(1.2, self.thrall.berserk_factor)

    def test_berserk_factor_within_bounds(self):
        normal_berserking_orc = Orc("Aaaaaa", 100, 1.89)
        self.assertEqual(1.89, normal_berserking_orc.berserk_factor)

    def test_berserk_factor_out_of_bounds(self):
        berserking_orc = Orc("Gromash", 100, 3)
        self.assertEqual(2, berserking_orc.berserk_factor)

        less_berserking_orc = Orc("Not Gromash", 100, -20)
        self.assertEqual(1, less_berserking_orc.berserk_factor)

    def test_attack_with_berserk_factor(self):
        self.thrall.equip_weapon(Weapon("Pickaxe", 38, 0.6))
        self.assertEqual(self.thrall.weapon.damage * self.thrall.berserk_factor,
                         self.thrall.attack())

if __name__ == '__main__':
    unittest.main()
