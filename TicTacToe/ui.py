class UI:
    SIZE = 3
    BOARD = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    def print_map(self):
        for each in self.BOARD:
            for cell in each:
                print('[{}] '.format(cell), end='')
            print()
