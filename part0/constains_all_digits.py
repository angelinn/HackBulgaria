from constains_digit import contains_digit

def contains_all_digits(number, digits):
    for each in digits:
        if contains_digit(number, each) == False:
            return False

    return True

print(contains_all_digits(456, []))