from is_prime import is_prime


def goldbach(n):
    result = []
    limit = n

    for i in range(2, limit):
        print("I IS " + str(i))
        for j in range(i + 1, n):
            print(j)
            if is_prime(j) is True:
                print("IN FIRST IF")
                first = j
                n -= first
                print(first)
                print(n)
                for j in range(n, 0, -1):
                    print(str(j) + " is")
                    if is_prime(j) and n - j == 0:
                        print("IN SECOND IF")
                        result.append((first, j))
                        break

    if len(result) == 0:
        return False

    return result


def main():
    print(goldbach(100))

if __name__ == '__main__':
    main()
