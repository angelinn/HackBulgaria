import sqlite3


class CompanyControl:
    DATABASE_NAME = 'employees.db'

    def __init__(self):
        self.database = None
        self.cursor = None

        self.load_database()

    def load_database(self):
        try:
            self.database = sqlite3.connect(self.DATABASE_NAME)
            self.cursor = self.database.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                                   employees(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER,
                                   yearly_bonus INTEGER, position TEXT)''')
            self.database.commit()

        except Exception:
            self.database.rollback()
            self.database.close()
            raise Exception

    def fill_database(self):
        self.cursor.execute('DELETE FROM employees')

        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', ('Ivan Ivanov', 5000, 10000, 'Software Developer'))
        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', ('Rado Rado', 500, 0, 'Technical Support Intern'))
        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', ('Ivo Ivo', 10000, 100000, 'CEO'))
        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', ('Petar Petrov', 3000, 1000, 'Marketing Manager'))
        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', ('Maria Georgieva', 8000, 10000, 'COO'))

        self.database.commit()

    def add_employee(self):
        data = self.input_fields()

        name = data[0]
        salary = data[1]
        bonus = data[2]
        position = data[3]

        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', (name, salary, bonus, position))
        self.database.commit()

    def delete_employee(self, id):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
        self.database.commit()

    def update_employee(self, id):
        data = self.input_fields()

        name = data[0]
        salary = data[1]
        bonus = data[2]
        position = data[3]

        self.cursor.execute('''UPDATE employees SET name = ?, monthly_salary = ?, yearly_bonus = ?,
         position = ? WHERE id = ?''',
                            (name, salary, bonus, position, id))

        self.database.commit()

    def monthly_spending(self):
        total_monthly = self.cursor.execute('SELECT SUM(monthly_salary) FROM employees').fetchone()
        return 'The company is spending {} per month.'.format(total_monthly[0])

    def yearly_spending(self):
        total_yearly = self.cursor.execute('SELECT SUM(yearly_bonus) FROM employees').fetchone()
        return 'The company is spending {} per year.'.format(total_yearly[0])

    def input_fields(self):
        data = []

        data.append(input("Name > "))
        data.append(input("Monthly Salary > "))
        data.append(input("Yearly bonus > "))
        data.append(input("Position > "))

        return data

    def list_employees(self):
        result = self.cursor.execute('SELECT * FROM employees')
        a = result.fetchall()

        for row in a:
            print('[{}] {} - {}'.format(row[0], row[1], row[4]))

    def go(self):
        while True:
            command = input("> ")

            if command == 'add_employee':
                self.add_employee()
            elif command.split()[0] == 'delete_employee':
                self.delete_employee(command.split()[1])
            elif command.split()[0] == 'update_employee':
                self.update_employee(command.split()[1])
            elif command == 'list_employees':
                self.list_employees()
            elif command == 'monthly_spending':
                print(self.monthly_spending())
            elif command == 'yearly_spending':
                print(self.yearly_spending())
            elif command == 'exit':
                break

        self.database.close()


def main():
    CompanyControl().go()

if __name__ == '__main__':
    main()
