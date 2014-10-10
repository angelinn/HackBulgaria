from sum_of_digits import sum_of_digits
import math


def is_number_balanced(number):
    length = int(math.log10(number)) + 1
    number = str(number)
    first_part = ""
    second_part = ""

    if length % 2 != 0:
        first_part = number[:length // 2]
        second_part = number[(length + 1) // 2:]
    else:
        first_part = number[:length // 2]
        second_part = number[length // 2:]

    number = first_part + second_part

    if sum_of_digits(int(first_part)) == sum_of_digits(int(second_part)):
        return True
    else:
        return False
