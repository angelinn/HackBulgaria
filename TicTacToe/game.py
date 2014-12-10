from ai import AI
from ui import UI


class Game:

    def __init__(self):
        self.enemy = AI()
        self.player = None

        self.UI = UI()

    def input_choice(self):
        x = int(input('x: '))
        y = int(input('y: '))

        if x >= self.UI.SIZE or y >= self.UI.SIZE:
            raise ValueError

        return (x, y)

    def start(self):
        choice = None

        while True:
            self.UI.print_map()

            try:
                choice = self.input_choice()
            except ValueError:
                continue

            print('{} {}'.format(choice[0], choice[1]))
            self.UI.BOARD[choice[0]][choice[1]] = 'X'

    def go(self):
        print('{} {} {}\nWrite start to play!'.format('-' * 10, 'Tic Tac Toe!', '-' * 10))

        if input('> ') == 'start':
            self.start()

Game().go()
