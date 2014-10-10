def fraction_to_float(fraction):
    return fraction[0] / fraction[1]


def sort_fractions(fractions):
    length = len(fractions)

    for i in range(length):
        for j in range(length - 1):
            if fraction_to_float(fractions[i]) < fraction_to_float(fractions[j]):
                swap = fractions[i]
                fractions[i] = fractions[j]
                fractions[j] = swap

    return fractions

print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
