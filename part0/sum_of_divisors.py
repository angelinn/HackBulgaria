def sum_of_divisors(n):
    divisors = 0

    i = 1

    while i <= n:
        if n % i == 0:
            divisors += i
        i += 1

    return divisors


print(sum_of_divisors(10))
