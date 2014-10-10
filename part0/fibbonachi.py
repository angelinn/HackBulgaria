def nth_fibbonachi(n):
    first = 0
    second = 1

    for i in range(n - 1):
        result = first + second
        first = second
        second = result

    return result
