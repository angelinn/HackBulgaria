def contains_digit(number, digit):
    if number == 0:
        return False

    if number % 10 == digit:
        return True

    return contains_digit(number // 10, digit)
