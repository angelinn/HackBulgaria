def prepare_meal(n):
    result = ""

    while n > 0:
        if n % 3 == 0:
            result = "spam " + result
            n //= 3
        elif n % 5 == 0:
            if result == "":
                result = "eggs "
            else:
                result = result + "and eggs "
            n //= 5
        else:
            break

    return result

print(prepare_meal(45))
