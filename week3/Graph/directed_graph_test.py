import unittest
from directed_graph import DirectedGraph
from node import Node


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.node_one = Node('Penko')
        self.node_two = Node('Penka')

        self.graph = DirectedGraph()

    def test_add_edge(self):
        self.graph.add_edge(self.node_one, self.node_two)
        self.assertIn(self.node_one, self.graph.nodes[self.node_two.name].is_pointed_by)
        self.assertIn(self.node_two, self.graph.nodes[self.node_one.name].points_to)

    def test_get_neighbours_for(self):
        pencho = Node('Pencho')

        self.graph.add_edge(self.node_one, self.node_two)
        self.graph.add_edge(self.node_one, pencho)
        self.assertEqual([self.node_two, pencho], self.graph.get_neighbours_for(self.node_one))

    def test_path_between_normal(self):
        self.graph.add_edge(self.node_one, self.node_two)
        self.assertTrue(self.graph.path_between(self.node_one, self.node_two))
        self.assertFalse(self.graph.path_between(self.node_two, self.node_one))

    def test_path_between_rare(self):
        penichka = Node('Penichka')
        self.graph.add_edge(self.node_one, self.node_two)
        self.graph.add_edge(self.node_two, penichka)
        self.assertTrue(self.graph.path_between(self.node_one, penichka))

    def test_path_between_recursion(self):
        uno = Node('1')
        dos = Node('2')
        tres = Node('3')
        quatro = Node('4')
        cinco = Node('5')
        seis = Node('6')

        self.graph.add_edge(uno, dos)
        self.graph.add_edge(dos, tres)
        self.graph.add_edge(dos, quatro)
        self.graph.add_edge(quatro, cinco)
        self.graph.add_edge(quatro, seis)
        self.graph.add_edge(tres, dos)

        self.assertTrue(self.graph.path_between(uno, seis))

if __name__ == '__main__':
    unittest.main()
