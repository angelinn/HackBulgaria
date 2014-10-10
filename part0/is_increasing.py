def is_increasing(seq):
    length = len(seq)

    for i in range(length):
        for j in range(i + 1, length):
            if seq[j] <= seq[i]:
                return False

    return True