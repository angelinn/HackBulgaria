def fibonacci_lists(listA, listB, n):
    first = listA
    second = listB

    if n == 1:
        return first
    if n == 2:
        return second

    for i in range(2, n):
        result = first + second
        first = second
        second = result

    return result


def main():
    print(fibonacci_lists([1, 2], [3, 4], 5))

if __name__ == '__main__':
    main()
