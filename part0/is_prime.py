def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n == 1:
        return False

    i = 3
    top = n / 2

    while i <= top:
        if n % i == 0:
            return False

        i += 1

    return True
