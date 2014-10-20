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
            while True:
                if self.orc.is_alive() is False:
                    print("{0} has died. {1} has won the battle".format(self.orc.name,
                                                                        self.hero.known_as()))
                    return 1
                elif self.hero.is_alive() is False:
                    print("{0} has died. {1} has won the battle".format(self.hero.known_as(),
                                                                        self.orc.name))
                    return -1

                self.orc.take_damage(self.hero.attack())
                print("{0} got hit for {1} damage by {2}.".format(self.orc.name,
                      self.hero.attack(), self.hero.known_as()))
                self.hero.take_damage(self.orc.attack())
                print("{0} got hit for {1} damage by {2}.".format(self.hero.known_as(),
                      self.hero.attack(), self.orc.name))
