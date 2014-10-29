import requests
from pprint import pprint


class WhoIsFollowingMe:
    def __init__(self):
        self.followers_dict = {}
        self.following_dict = {}

    def following(self, user):
        print('aaaaaaaaaaaaaaaaaaaa')
        req = requests.get('https://api.github.com/users/{0}/followers?client_id=946eccaded95518a57e5&client_secret=09915ff70cda2018b3dd3ca69f109e3ff892ea33'.format(user))
        if req.status_code != 200:
            raise ValueError

        print('YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        data = req.json()

        pprint(data)


WhoIsFollowingMe().following('betrakiss')
