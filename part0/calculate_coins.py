def calculate_coins(num):

    result = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
    coins = [1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

    for item in coins:
        while num > 0:
            if num - item >= 0:
                result[str(int(item * 100))] += 1
                num -= item
            else:
                break

    return result
