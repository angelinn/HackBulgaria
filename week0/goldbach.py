from is_prime import is_prime


def goldbach(n):
    result = []
    limit = n

    for i in range(2, limit):
        for j in range(i + 1, n):
            if is_prime(j) is True:
                first = j
                n -= first
                print("N is " + str(n))
                print("First is " + str(first))

                for j in range(n, 0, -1):
                    if is_prime(j) and n - j == 0:
                        result.append((first, j))
                        break
                break

        n = limit

    if len(result) == 0:
        return False

    return result


def main():
    print(goldbach(100))

if __name__ == '__main__':
    main()
