class Fraction:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __eq__(self, other):
        return self.denum == other.denum and self.num == other.num

    def __add__(self, other):
        result = Fraction(self.num * other.denum, self.denum * other.denum)
        result.num += other.num * self.denum

        return result

    def __sub__(self, other):
        result = Fraction(self.num * other.denum, self.denum * other.denum)
        result.num -= other.num * self.denum

        return result

    def __lt__(self, other):
        if self.denum == other.denum:
            return self.num < other.num

        return self.num * other.denum < other.num * self.denum

    def __gt__(self, other):
        if self.denum == other.denum:
            return self.num > other.num

        return not self < other

    def __str__(self):
        return "{} / {}".format(self.num, self.denum)


def main():
    uno = Fraction(1, 2)
    dos = Fraction(3, 4)

    print(uno == dos)
    print(uno > dos)
    print(uno < dos)
    print(uno + dos)
    print(uno - dos)

if __name__ == '__main__':
    main()
