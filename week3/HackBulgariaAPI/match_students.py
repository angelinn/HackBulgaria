import requests
import random


class TeamMatcher:
    def __init__(self):
        self.data = []
        self.courses = []

    def read_data(self):
        reqs = requests.get('https://hackbulgaria.com/api/students/', verify=False)

        if reqs.status_code != 200:
            raise ValueError

        self.data = reqs.json()
        #pprint.pprint(self.data)

    def read_courses(self):
        for person in self.data:
            for course in person['courses']:
                if course['name'] not in self.courses:
                    self.courses.append(course['name'])

    def list_courses(self):
        for i, course in enumerate(self.courses):
            print('[{0}] {1}'.format(i, course))

    def match_teams(self, course_id, team_size, group_time):
        random.shuffle(self.courses)

        for person in self.data:
            for i in range(team_size):
                for course in person['courses']:
                    if course['name'] == self.courses[course_id] and course['group'] == group_time:
                        print(person['name'])
        print('=============')






t = TeamMatcher()
t.read_data()
t.read_courses()
t.list_courses()
t.match_teams(4, 2, 2)
