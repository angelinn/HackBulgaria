from random import random


class Fight:
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def flip_coin(self):
        if random() < 0.5:
            return "Hero"

    def simulate_fight(self):
        if self.flip_coin() == "Hero":
            attacker = self.hero
            defender = self.orc

        else:
            attacker = self.orc
            defender = self.hero

        while True:
            if defender.is_alive() is False:
                print("{0} has died. {1} has won the battle".format(defender.name,
                                                                    attacker.name))
                return 1
            elif attacker.is_alive() is False:
                print("{0} has died. {1} has won the battle".format(attacker.name,
                                                                    defender.name))
                return -1

            attacker_damage = attacker.attack()
            defender_damage = defender.attack()

            defender.take_damage(attacker_damage)
            self.print_stats(attacker, defender, attacker_damage, defender_damage)

            attacker.take_damage(defender_damage)
            self.print_stats(defender, attacker, defender_damage, attacker_damage)

            input('> ')

    def print_stats(self, attacker, defender, attacker_damage, defender_damage):
        print("\t.:: {0} <Health: {1}> ::.\n\t    got hit for {2} damage by\n\t.:: {3} <Health: {4}> ::.\n"
              .format(defender.name, defender.health, attacker_damage, attacker.name, attacker.health))
