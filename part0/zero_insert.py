from number_to_list import number_to_list
from list_to_number import list_to_number


def zero_insert(number):
    number = number_to_list(number)
    length = len(number)

    number_to_insert = 0

    i = 0
    while i < length - 1:
        if number[i] == number[i + 1] or ((number[i] + number[i + 1]) % 10 == 0):
            number.insert(i + 1, number_to_insert)
            length += 1
            i += 1

        i += 1

    return list_to_number(number)

print (zero_insert(6446))
