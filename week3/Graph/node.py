class Node:
    def __init__(self, name):
        self.name = name
        self.points_to = []
        self.is_pointed_by = []
        self.available = True

    def add_follower(self, follower):
        self.is_pointed_by.append(follower)

    def follow(self, leader):
        self.points_to.append(leader)
