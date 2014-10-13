import math


def number_length(number):
    if number < 10:
        return 1

    return int(math.log10(number)) + 1
