def sum_line(line):
    total = 0
    for each in line:
        total += each

    return total


def magic_square(matrix):
    target = sum_line(matrix[0])

    for line in matrix:
        if not check_line(line, target):
            return False

    total = 0
    for i, j in range(len(matrix[0])):
        total += matrix[i][j]

    if total != target:
        return False


