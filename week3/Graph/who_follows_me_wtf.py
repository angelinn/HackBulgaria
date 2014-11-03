import requests
from node import Node
from directed_graph import DirectedGraph
from pprint import pprint


class WhoIsFollowingMe:
    def __init__(self):
        self.user = DirectedGraph()

    def following(self, user):
        url = 'https://api.github.com/users/{0}/followers?client_id=946eccaded95518a57e5&client_secret=09915ff70cda2018b3dd3ca69f109e3ff892ea33'.format(user)
        req = requests.get(url)
        if req.status_code != 200:
            raise ValueError

        data = req.json()

        usr = Node(user)

        for each in data:
            self.being_followed.add_edge(Node(each['login']), usr)

        print(self.being_followed)
        #pprint(data)


WhoIsFollowingMe().following('Ivaylo-Bachvarov')
