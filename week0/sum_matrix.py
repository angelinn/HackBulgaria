def sum_matrix(m):
    total = 0

    for each in m:
        total += sum_digits_list(each)

    return total


def sum_digits_list(list):
    total = 0

    for each in list:
        total += each

    return total

print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
