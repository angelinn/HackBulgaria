def prepare_meal(n):
    result = ""
    more_than_once = False

    while n > 0:
        if n % 3 == 0:
            if more_than_once is True:
                result = "spam " + result
            else:
                result = "spam" + result
            n //= 3

            more_than_once = True

        elif n % 5 == 0:
            if result == "":
                result = "eggs"
            else:
                result = result + " and eggs"
            n //= 5
        else:
            break

    return result

print(prepare_meal(25))
