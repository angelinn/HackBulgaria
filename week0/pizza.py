def take(details, orders):
    name = details[1]
    price = details[2]

    if name in orders:
        orders[name] += price
    else:
        orders[name] = price

    print("Taking order from " + name + " for " + str(price))


def order():
    command = ''
    orders = {}

    while command != 'finish':
        command = input("Enter a command .. ")
        if command.find('take') != -1:
            take(command.split(' '), orders)

    print(orders)

    return True


def main():
    order()


if __name__ == '__main__':
    main()
