from constains_digit import contains_digit


def contains_all_digits(number, digits):
    for each in digits:
        if contains_digit(number, each) is False:
            return False

    return True
