from nan_expand import nan_expand


def iterations_on_nan_expand(string):
    if string.find("Not a NaN") == -1:
        return False

    i = 0
    while i >= 0:
        if string == nan_expand(i):
            return i

        i += 1
