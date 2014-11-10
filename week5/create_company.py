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
        name = input("Name > ")
        salary = input("Monthly Salary > ")
        bonus = input("Yearly bonus > ")
        position = input("Position > ")

        self.cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', (name, salary, bonus, position))
        self.database.commit()

    def go(self):
        while True:
            command = input("> ")

            if command == 'add_employee':
                self.add_employee()
            elif command == 'exit':
                break

        result = self.cursor.execute('SELECT * FROM employees')
        a = result.fetchall()
        print(a)
        self.database.close()


def main():
    CompanyControl().fill_database()

if __name__ == '__main__':
    main()
