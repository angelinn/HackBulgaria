def is_decreasing(seq):
    length = len(seq)

    for i in range(length):
        for j in range(i + 1, length):
            if seq[j] >= seq[i]:
                return False
    return True


print(is_decreasing([5, 4, 3, 2, 6, 1]))