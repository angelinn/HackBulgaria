import copy


def check_column(sudoku, column_number, target):
    target_copy = copy.deepcopy(target)

    for j in range(len(sudoku)):
        for number in target_copy:
            print(str(sudoku[column_number][j]) + ' vs ' + str(number))
            if sudoku[column_number][j] == number:
                print(target_copy.remove(number))

    print(target_copy)
    return target_copy == []


def check_line(line, target):
    target_copy = copy.deepcopy(target)

    for each in line:
        for number in target_copy:
            if each == number:
                target_copy.remove(number)

    print(target_copy)
    return target_copy == []


def sudoku_solved(sudoku):
    target = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i, line in enumerate(sudoku):
        if check_line(line, target) is False or check_column(sudoku, i, target) is False:
            print("This line didn't pass the test: " + str(line))
            return False
        else:
            print("This line has passed test : " + str(line))

    print("Motherfucking Sudoku !!")


def main():
    sudoku_solved([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
])


if __name__ == '__main__':
    main()
