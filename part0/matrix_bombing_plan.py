from sum_matrix import sum_matrix
import copy


def bomb(matrix, i, j, core):
    if i >= len(matrix[0]) or i < 0 or j >= len(matrix) or j < 0:
        return False

    if matrix[i][j] - core < 0:
        matrix[i][j] = 0
    else:
        matrix[i][j] -= core


def matrix_bombing_plan(matrix):
    m = len(matrix)
    n = len(matrix[0])

    original_matrix = copy.deepcopy(matrix)
    results = {}

    for i in range(m):
        for j in range(n):
            print("i = " + str(i) + " j = " + str(j))
            matrix = copy.deepcopy(original_matrix)
            print("Refreshing Matrix .. ")
            print(matrix)

            bomb(matrix, i + 1, j, matrix[i][j])
            bomb(matrix, i - 1, j, matrix[i][j])
            bomb(matrix, i, j + 1, matrix[i][j])
            bomb(matrix, i + 1, j + 1, matrix[i][j])
            bomb(matrix, i - 1, j + 1, matrix[i][j])
            bomb(matrix, i, j - 1, matrix[i][j])
            bomb(matrix, i + 1, j - 1, matrix[i][j])
            bomb(matrix, i - 1, j - 1, matrix[i][j])

            results[(i, j)] = sum_matrix(matrix)

    return results
