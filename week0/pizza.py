from time import time
from datetime import datetime


def take(details, orders):
    name = details[1]
    price = details[2]

    if name == '' or price == '':
        print("Invalid value entered.")
        return False

    if name in orders:
        orders[name] += price
    else:
        orders[name] = price

    print("Taking order from {0} for {1}".format(name, price))
    return True


def status(orders):
    print(orders)
    for each in orders:
        print('{0}: {1}'.format(each, orders[each]))


def save(orders, file_names):
    ts = time()
    stamp = 'orders_' + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    save_file = open(stamp, 'w')
    for each in orders:
        save_file.write('{0} {1}\n'.format(each, orders[each]))

    save_file.close()

    names = open(file_names, 'a+')
    names.write(stamp + '\n')
    names.close()

    print("Saved.")


def list(files_names):
    names = open(files_names, 'r')
    content = names.read().split('\n')

    for i in range(len(content)):
        if content[i] != '':
            print('{0}{1}{2} = {3}'.format('[', i, ']', content[i]))

    return content


def load(files, number):
    orders_file = open(files[number], 'r')
    content = orders_file.read().split('\n')
    new_orders = {}

    for each in content:
        if each != '':
            each = each.split(' ')
            new_orders[each[0]] = float(each[1])

    return new_orders


def order():
    file_names = "files.txt"
    command = ''
    orders = {}
    files = []

    while command != 'finish':
        print(orders)
        command = input("Enter a command .. ")
        if command.find('take') != -1:
            take(command.split(' '), orders)
        if command == 'status':
            status(orders)
        if command == 'save':
            save(orders, file_names)
        if command == 'list':
            files = list(file_names)
        if command.find('load') != -1:
            orders = load(files, float(command.split(' ')[1]))

    print(orders)

    return True


def main():
    order()


if __name__ == '__main__':
    main()
