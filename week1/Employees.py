class Employee:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def weeklyPay(self, hours):
        return "uuuh ! Money!"


class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        super().__init__(name, wage)

    def weeklyPay(self, hours):
        if hours > 40:
            return (self.wage * hours) * 1.5

        return self.wage * hours


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def weeklyPay(self, hours):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary + self.bonus


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff:
        hours = int(input("Hours worked by " + employee.name + ": "))
        pay = employee.weeklyPay(hours)
        print("Salary: %.2f" % pay)

if __name__ == '__main__':
    main()
