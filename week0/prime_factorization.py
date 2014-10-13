from is_prime import is_prime


def prime_factorization(n):
    if is_prime(n):
        return [(n, 1)]

    result = []

    for i in range(2, n):
        times_divided = 0
        print("Starting ..")
        print(n)
        if n % i == 0:
            times_divided += 1
            n //= i

        if times_divided > 0:
            print("Appending .. ")
            result.append((i, times_divided))

    return result

print(prime_factorization(7))
