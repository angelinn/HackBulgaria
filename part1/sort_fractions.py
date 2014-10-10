from simplify_fraction import simplify_fraction


def sort_fractions(fractions):
    result = []
    length = len(fractions)

    for i in range(length):
        for j in range(length - 1):
            if simplify_fraction(fractions[i])[1]

    result.sort()
    return result

print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
