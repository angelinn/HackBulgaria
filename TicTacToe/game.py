from ai import AI
from ui import UI


class Game:
    welcome_message = '\n{} {} {}\nWrite start to play or exit to quit!'.format(
                      '-' * 10, 'Tic Tac Toe!', '-' * 10)

    winner_message = 'Game Over! Winner is {}'

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
        x = int(self.UI.get_input('x: '))
        y = int(self.UI.get_input('y: '))

        if self.are_x_y_valid(x, y) or self.UI.BOARD[x][y] != ' ':
            raise ValueError

        return (x, y)

    def are_x_y_valid(self, x, y):
        return x >= self.UI.SIZE or y >= self.UI.SIZE or x < 0 or y < 0

    def start(self):
        while self.game_over is False:
            self.UI.print_map()

            self.tick()

    def tick(self):
        try:
            choice = self.input_choice()

        except ValueError:
            self.UI.display('\nInvalid input! Please reenter.\n')
            return

        self.UI.BOARD[choice[0]][choice[1]] = self.UI.X

        if self.is_board_full():
            self.trigger_game_over(None)
            return

        self.AI.attack()

        is_there_a_winner = self.check_for_winner()

        if is_there_a_winner is not False:
            self.trigger_game_over(is_there_a_winner)
            return

    def check_for_winner(self):
        for route in self.winning_routes:
            if all(self.UI.BOARD[coords[0]][coords[1]] == self.UI.X for coords in route):
                return self.UI.X

            if all(self.UI.BOARD[coords[0]][coords[1]] == self.UI.O for coords in route):
                return self.UI.O

        return False

    def is_board_full(self):
        return all(all(block != ' ' for block in line) for line in self.UI.BOARD)

    def trigger_game_over(self, winner):
        self.game_over = True
        self.UI.print_map()
        self.UI.display(self.winner_message.format('Player' if winner == self.UI.X else
                                                   ('Enemy' if winner == self.UI.O else winner)))

    def go(self):
        self.UI.display(self.welcome_message)

        if self.UI.get_input('> ') == 'start':
            self.start()

if __name__ == '__main__':
    Game().go()
