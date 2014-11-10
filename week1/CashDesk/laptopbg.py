class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, disk_space, ram):
        super().__init__(name, stock_price, final_price)
        self.disk_space = disk_space
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, megapixels):
        super().__init__(name, stock_price, final_price)

        self.display_size = display_size
        self.megapixels = megapixels


class Store:
    products = {}
    income = 0

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            if product in self.products:
                self.products[product] += count
            else:
                self.products[product] = count

    def list_products(self, product_type):
        for each in self.products:
            if isinstance(each, product_type):
                print(each.name + ' - ' + str(self.products[each]))

    def sell_product(self, product, amount):
        if product in self.products and (self.products[product] - amount) >= 0:
            self.products[product] -= amount
            self.income += product.profit() * amount
            return True

        return False

    def total_income(self):
        return self.income


def main():
    store = Store("Prodavalnik.com")
    my_laptop = Laptop("Toshiba", 1000, 1800, 260, 2048)
    my_phone = Smartphone("HTC", 800, 900, 280, 6000)

    store.load_new_products(my_laptop, 8)
    store.load_new_products(my_laptop, 2)
    store.load_new_products(my_phone, 3)
    store.list_products(Product)
    store.sell_product(my_phone, 2)
    store.list_products(Product)
    print(store.total_income())

if __name__ == '__main__':
    main()
