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


def save(orders, file_names):
    ts = time()
    stamp = 'orders_' + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    save_file = open(stamp, 'w')
    for each in orders:
        save_file.write(each + ' ' + str(orders[each]) + '\n')

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


def load(files, number, orders):
    print(files)
    print(number)
    orders_file = open(files[number], 'r')
    content = orders_file.read().split('\n')
    new_orders = {}

    for each in content:
        each = each.split(' ')
        new_orders[each[0]] = int(each[1])

    orders = new_orders
    return orders


def order():
    file_names = "files.txt"
    command = ''
    orders = {}
    files = []

    while command != 'finish':
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
            print(command)
            load(files, int(command.split(' ')[1]), orders)

    print(orders)

    return True


def main():
    order()


if __name__ == '__main__':
    main()
