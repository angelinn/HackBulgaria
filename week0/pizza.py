from time import time
from datetime import datetime


class Pizza:
    file_names = "files.txt"
    command = ''
    orders = {}
    files = []
    display_warning = False

    def take(self, details):
        self.display_warning = True

        name = details[1]
        price = details[2]

        if name == '' or price == '':
            raise ValueError

        if name in self.orders:
            self.orders[name] += price
        else:
            self.orders[name] = price

        print("Taking order from {0} for {1}".format(name, price))
        return True

    def status(self):
        for each in self.orders:
            print('{0}: {1}'.format(each, self.orders[each]))

    def save(self):
        if self.orders == {}:
            print("Orders are empty. Please order something first!")

        ts = time()
        stamp = 'orders_' + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        save_file = open(stamp, 'w')
        print(self.orders)
        for each in self.orders:
            save_file.write('{0} {1}\n'.format(each, self.orders[each]))

        save_file.close()

        names = open(self.file_names, 'a+')
        names.write(stamp + '\n')
        names.close()

        self.display_warning = False
        print("Saved.")

    def list(self):
        names = open(self.file_names, 'r')
        content = names.read().split('\n')

        for i in range(len(content)):
            if content[i] != '':
                print('{0}{1}{2} = {3}'.format('[', i, ']', content[i]))

        names.close()
        return content

    def load(self, number):
        if self.files == []:
            print("You must use the 'list' command first before loading.")
            return False

        if self.display_warning is True:
            print("You have not saved your current list. If you want to continue type load again")
            self.display_warning = False
            return False

        print("Loading {0} ..".format(self.files[number]))
        orders_file = open(self.files[number], 'r')
        content = orders_file.read().split('\n')
        new_orders = {}

        for each in content:
            if each != '':
                each = each.split(' ')
                new_orders[each[0]] = float(each[1])

        return new_orders

    def help(self):
            print("""
                Available commands:

                take <name> <price> - starts an order
                status - displays orders
                save - saves orders
                help - displays this pro text
                list - displays saved orders
                load <number> - loads number from 'list'
                clear - clear the 'list'
                finish - exits the pro program
                """)

    def order(self):
        while True:
            try:
                command = input("Enter a command > ")
                if command.find('take') != -1:
                    self.take(command.split(' '))

                elif command == 'status':
                    self.status()

                elif command == 'save':
                    self.save()

                elif command == 'list':
                    self.files = self.list()

                elif command.find('load') != -1:
                    self.orders = self.load(int(command.split(' ')[1]))

                elif command == 'clear':
                    trunc = open(self.file_names, 'w')
                    trunc.close()

                elif command == 'help':
                    self.help()

                elif command == 'finish':
                    if self.display_warning is True:
                        print("You have not saved. Type finish again to continue")
                        self.display_warning = False
                    else:
                        print("Bye Bye!")
                        break
                else:
                    print("Unknown command!")

            except ValueError:
                print("Invalid value.")
            except BaseException:
                print("Something isn't right ..")

        return True

Pizza().order()
