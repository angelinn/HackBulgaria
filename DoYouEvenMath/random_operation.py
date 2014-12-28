from random import randint


class RandomOperation:
    TOO_HIGH_POWER = 5

    def __init__(self, a, b, result=None):
        self.a = a
        self.b = b
        self.sign = self.get_random_sign()
        self.result = result

    def get_random_sign(self):
        signs = ['*', '+', '-', '//', '^']
        return signs[randint(0, 4)]

    def do_real_operation(self):
        if self.sign == '^':
            if self.b > self.TOO_HIGH_POWER:
                self.b = randint(0, 3)

            self.result = pow(self.a, self.b)

        else:
            try:
                self.result = eval('{} {} {}'.format(self.a, self.sign, self.b))

            except ZeroDivisionError:
                while self.b == 0:
                    self.b = randint(0, 20)

                    self.result = eval('{} {} {}'.format(self.a, self.sign, self.b))
