from is_prime import is_prime


def goldbach(n):
    result = []
    limit = n

    for i in range(2, (limit // 2) + 1):
        if is_prime(i) is True:
            first = i
            n -= first

            for j in range(n, 0, -1):
                if is_prime(j) and n - j == 0:
                    result.append((first, j))
                    i = first
                    break

        n = limit

    if len(result) == 0:
        return False

    return result


def main():
    print(goldbach(4))

if __name__ == '__main__':
    main()
