#from node import Node


class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_a, node_b):
        if node_a.name not in self.nodes:
            self.nodes[node_a.name] = node_a

        self.nodes[node_a.name].follow(node_b)

        if node_b not in self.nodes:
            self.nodes[node_b.name] = node_b

        self.nodes[node_b.name].add_follower(node_a)

    def get_neighbours_for(self, node):
        return self.nodes[node.name].points_to

    def path_between(self, node_a, node_b):
        if node_a.name not in self.nodes or node_b.name not in self.nodes:
            return False

        if self.nodes[node_a.name].points_to == []:
            return False

        if node_b in self.nodes[node_a.name].points_to:
            return True

        for i in range(len(self.nodes[node_a.name].points_to)):
            if self.nodes[node_a.name].points_to[i].available is True:
                self.nodes[node_a.name].points_to[i].available = False
            else:
                continue

            if self.path_between(self.nodes[node_a.name].points_to[i], node_b) is True:
                return True
