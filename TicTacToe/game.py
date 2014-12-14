from ai import AI
from ui import UI


class Game:

    winning_routes = [[(0, 0), (0, 1), (0, 2)],
                      [(0, 0), (1, 0), (2, 0)],
                      [(0, 0), (1, 1), (2, 2)],
                      [(1, 0), (1, 1), (1, 2)],
                      [(0, 1), (1, 1), (2, 1)],
                      [(0, 2), (1, 2), (2, 2)],
                      [(2, 0), (2, 1), (2, 2)],
                      [(2, 0), (1, 1), (0, 2)]]

    def __init__(self):
        self.UI = UI()

        self.AI = AI(self.UI.BOARD, self.winning_routes)
        self.player = None
        self.game_over = False

    def input_choice(self):
        x = int(input('x: '))
        y = int(input('y: '))

        if self.are_x_y_valid(x, y) or self.UI.BOARD[x][y] != ' ':
            raise ValueError

        return (x, y)

    def are_x_y_valid(self, x, y):
        return x >= self.UI.SIZE or y >= self.UI.SIZE or x < 0 or y < 0

    def start(self):
        while self.game_over is False:
            self.UI.print_map()

            if self.check_for_winner() is not None:
                self.print_winner(self.check_for_winner())
                break

            self.tick()

    def tick(self):
        try:
            choice = self.input_choice()

        except ValueError:
            print('\nInvalid input! Please reenter.\n')
            return

        self.UI.BOARD[choice[0]][choice[1]] = 'X'

        if self.is_board_full():
            print("Game over! It's a draw!")
            return

        self.AI.attack()

    def check_for_winner(self):
        sign = None
        met = 0

        for route in self.winning_routes:
            for item in route:
                if sign is None and self.UI.BOARD[item[0]][item[1]] != ' ':
                    sign = self.UI.BOARD[item[0]][item[1]]
                    met += 1
                    continue

                if self.UI.BOARD[item[0]][item[1]] == sign:
                    met += 1

                if met == 3:
                    return sign

            met = 0
            sign = None

    def is_board_full(self):
        for row in self.UI.BOARD:
            for place in row:
                if place == ' ':
                    return False

        self.game_over = True
        return True

    def print_winner(self, sign):
        print('Winner is: {}'.format('Player' if sign == 'X' else 'Enemy'))

    def go(self):
        welcome_message = '\n{} {} {}\nWrite start to play or exit to quit!'.format(
            '-' * 10, 'Tic Tac Toe!', '-' * 10)

        print(welcome_message)

        while input('> ') == 'start':
            self.start()
            print(welcome_message)

if __name__ == '__main__':
    Game().go()
