from random import randint


class AI:

    def __init__(self, BOARD, winning_routes):
        self.BOARD = BOARD
        self.winning_routes = winning_routes

    def get_best_position(self):
        matches = 0
        free = (-1, -1)

        for route in self.winning_routes:
            for item in route:
                if self.BOARD[item[0]][item[1]] == 'X':
                    matches += 1

                elif self.BOARD[item[0]][item[1]] == ' ':
                    free = item

            if matches == 2:
                if free == (-1, -1):
                    continue

                return free

            matches = 0
            free = (-1, -1)

        return False

    def attack(self):
        coords = self.get_best_position()

        if coords:
            self.BOARD[coords[0]][coords[1]] = 'O'

        else:
            while True:
                x = randint(0, 2)
                y = randint(0, 2)

                if self.BOARD[x][y] == ' ':
                    self.BOARD[x][y] = 'O'
                    break
