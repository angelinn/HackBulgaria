def list_to_number(digits):
    number = 0
    power = len(digits) - 1

    for each in digits:
        number += each * (10 ** power)
        power -= 1

    return number