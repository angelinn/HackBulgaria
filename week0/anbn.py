def is_an_bn(word):

    letter_counter = 0
    b_started = False

    if word == "":
        return True

    for letter in word:
        if letter == 'a':
            if b_started:
                return False

            letter_counter += 1
        elif letter == 'b':
            b_started = True
            letter_counter -= 1

    if letter_counter != 0:
        return False
    return True
