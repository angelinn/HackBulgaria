class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for each in money:
            self.money[each] += money[each]

        return self.money

    def total(self):
        total_money = 0
        for each in self.money:
            total_money += self.money[each] * each

        return total_money

    def can_withdraw_money(self, amount_of_money):
        values = [100, 50, 20, 10, 5, 2, 1]

        for each in values:
            if each == amount_of_money and self.money[each] > 0:
                self.money[each] -= 1
                return amount_of_money - each == 0

            print(each < amount_of_money)
            if each < amount_of_money:
                for i in range(self.money[each], 0, -1):
                    if each * i <= amount_of_money:
                        amount_of_money -= each * i
                        self.money[each] -= i

        return amount_of_money == 0


def main():
    cash_desk = CashDesk()
    cash_desk.take_money({1: 2, 50: 1, 20: 1})
    print(cash_desk.can_withdraw_money(10))

if __name__ == '__main__':
    main()
