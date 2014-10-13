def simplify_fraction(fraction):
    first = fraction[0]
    second = fraction[1]

    for i in range(max(first, second), 1, -1):
        while first % i == 0 and second % i == 0:
            first //= i
            second //= i

    return (first, second)

print(simplify_fraction((64, 462)))
