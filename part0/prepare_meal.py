def prepare_meal(n):
    result = ""

    while n > 0:
        if n % 3 == 0:
            "spam " + result
            n //= 3
        if n % 5 == 0:
            "and eggs " + result
            n //= 5

print(prepare_meal(3))
