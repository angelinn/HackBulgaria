def sum_line(line):
    total = 0
    for each in line:
        total += each

    return total


def check_lines(matrix, target):
    for line in matrix:
            if sum_line(line) != target:
                return False

    return True


def check_columns(matrix, target):
    for i in range(len(matrix)):
        column_total = 0
        for j in range(len(matrix[0])):
            column_total += matrix[i][j]

        return target == column_total


def check_middle(matrix, target):
    total = 0
    i = 0
    j = 0

    while i < len(matrix):
        total += matrix[i][j]
        i += 1
        j += 1

    if total != target:
        return False

    total = 0
    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    while i >= 0:
        total += matrix[i][j]
        i -= 1
        j -= 1

    return total == target


def magic_square(matrix):
    target = sum_line(matrix[0])

    if check_lines(matrix, target) is False:
        return False
    if check_columns(matrix, target) is False:
        return False
    if check_middle(matrix, target) is False:
        return False

    print("Passed final check! Is a fucking magic")
    return True


def main():
    print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))

if __name__ == '__main__':
    main()
