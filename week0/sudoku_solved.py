from copy import deepcopy

target = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


def check_number(number, target):
    if number in target:
        target[number] += 1
    else:
        target[number] = 1


def is_target_valid(target):
    counter = 0

    for number in target:
        counter += 1
        if target[number] != 1:
            return False

    return counter == 9


def check_column(sudoku, column_number):
    target_copy = deepcopy(target)

    for j in range(9):
        check_number(sudoku[column_number][j], target_copy)

    return is_target_valid(target_copy)


def check_line(line):
    target_copy = deepcopy(target)

    for number in line:
        check_number(number, target_copy)

    return is_target_valid(target_copy)


def sudoku_solved(sudoku):
    for i, line in enumerate(sudoku):
        if check_line(line) is False or check_column(sudoku, i) is False:
            #print("This line didn't pass the test: " + str(line))
            return False
        # else:
        #     print("This line has passed test : " + str(line))

    return True
    print("Motherfucking Sudoku !!")
