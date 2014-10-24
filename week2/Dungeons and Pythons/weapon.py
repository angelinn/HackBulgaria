from random import random


class Weapon:
    def __init__(self, type, damage, critical_percent):
        self.type = type
        self.damage = damage
        self.__set_critical_percent(critical_percent)

    def __set_critical_percent(self, critical_percent):
        if critical_percent > 1 or critical_percent < 0:
            raise ValueError

        self.critical_percent = critical_percent

    def critical_hit(self):
        return random() <= self.critical_percent
