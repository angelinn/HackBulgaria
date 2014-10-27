import requests
import random
from os import system


class TeamMatcher:

    _SEPARATOR = '==============='

    def __init__(self):
        self.data = []
        self.courses = []

    def read_data(self):
        reqs = requests.get('https://hackbulgaria.com/api/students/', verify=False)

        if reqs.status_code != 200:
            raise ValueError

        self.data = reqs.json()

    def read_courses(self):
        for person in self.data:
            for course in person['courses']:
                if course['name'] not in self.courses:
                    self.courses.append(course['name'])

        self.courses = sorted(self.courses)

    def list_courses(self):
        for i, course in enumerate(self.courses):
            print('[{0}] {1}'.format(i, course))

    def match_teams(self, course_id, team_size, group_time):
        random.shuffle(self.data)
        team_counter = 0

        for person in self.data:
            for course in person['courses']:
                if course['name'] == self.courses[course_id] and course['group'] == group_time:
                    print(person['name'])
                    team_counter += 1
                    if team_counter % team_size == 0:
                        print(self._SEPARATOR)

    def print_help(self):
        print('''list courses - this lists all the courses that are available now.
match teams <course_id>, <team_size>, <group_time>''')

    def go(self):
        print('loading data ..')
        self.read_data()
        self.read_courses()

        system('clear')
        while True:
            print("KUR")

        while True:
            command = input('> ')

            if command == 'help':
                self.print_help()
            elif command.find('match teams') != -1:
                res = command.split(' ')
                self.match_teams(int(res[2]), int(res[3]), int(res[4]))
            elif command == 'list courses':
                self.list_courses()
            elif command == 'exit':
                break
            else:
                print('Invalid command')


def main():
    TeamMatcher().go()

if __name__ == '__main__':
    main()
