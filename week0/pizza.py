from time import time
from datetime import datetime


def take(details, orders):
    name = details[1]
    price = details[2]

    if name in orders:
        orders[name] += price
    else:
        orders[name] = price

    print("Taking order from " + name + " for " + str(price))


def status(orders):
    for each in orders:
        print(each + ': ' + str(orders[each]))


def save(orders):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    save_file = open("orders_" + stamp, 'w')
    for each in orders:
        save_file.write(each + ' ' + str(orders[each]) + '\n')

    save_file.close()
    print("Saved.")


def order():
    command = ''
    orders = {}

    while command != 'finish':
        command = input("Enter a command .. ")
        if command.find('take') != -1:
            take(command.split(' '), orders)
        if command == 'status':
            status(orders)
        if command == 'save':
            save(orders)

    print(orders)

    return True


def main():
    order()


if __name__ == '__main__':
    main()
