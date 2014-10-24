from weapon import Weapon


class Entity():
    _NO_WEAPON = Weapon("None", 0, 0)

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = 100
        self.weapon = self._NO_WEAPON

    def get_health(self):
        return self.health

    def is_alive(self):
        return (self.health > 0)

    def take_damage(self, damage_points):
        if self.health - damage_points < 0:
            self.health = 0
        else:
            self.health -= damage_points

    def get_healing(self, healing_points):
        if self.is_alive() is False:
            return False

        if self.health + healing_points > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        else:
            self.health += healing_points

        return True

    def has_weapon(self):
        return self.weapon.type != 'None'

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon.critical_hit() is True:
            print("CRITICAL!")
            return self.weapon.damage * 2
        else:
            return self.weapon.damage
