def number_to_list(n):
    list_of_nums = []

    while n > 0:
        list_of_nums.append(n % 10)
        n //= 10

    list_of_nums = list_of_nums[::-1]

    return list_of_nums