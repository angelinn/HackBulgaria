from hero import Hero
from orc import Orc
from player import Player


class Dungeon:

    def __init__(self, file_name):
        self.players = {}
        self.map_list = []

        map_file = open(file_name, 'r')
        content = map_file.read().split('\n')

        for each in content:
            self.map_list.append(list(each))

        map_file.close()

    def print_map(self):
        for line in self.map_list:
            print(''.join(line))

    def spawn(self, player_name, entity):
        if player_name in self.players:
            raise ValueError

        self.players[player_name] = Player(player_name, entity, 0, 0)

        for i in range(len(self.map_list)):
            for j in range(len(self.map_list[0])):
                if self.map_list[i][j] == 'S':
                    if isinstance(self.players[player_name].entity, Hero):
                        self.map_list[i][j] = 'H'
                        self.players[player_name].set_position(i, j)
                        return True

                    elif isinstance(self.players[player_name].entity, Orc):
                        self.map_list[i][j] = 'O'
                        self.players[player_name].set_position(i, j)
                        return True

                    else:
                        raise TypeError

        return None
