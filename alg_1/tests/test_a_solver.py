import pytest
from alg import a_solver as a
from alg import graph as gr
from alg import dict_pq as dpq
from functools import total_ordering

class HeuristicGraph:
    """ Auxiliary class to create some heuristic function for
        A* search solver testing
    """

    def __init__(self, graph: gr.Graph):
        self._graph: gr.Graph = graph

    def get_h_val(self, vertex1, vertex2):
        return self._graph.get_weight(vertex1, vertex2) * .8
        # return 0


@total_ordering
class Vertex:
    """ Auxialiary class for testing purpose """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name 

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.name < other.name 

    def __hash__(self):
        return hash((self.name, ))

    def __repr__(self):
        return f"Vertex:{self.name}"


def test_1():
    g = gr.Graph()
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")
    v5 = Vertex("v5")
    v6 = Vertex("v6")
    v7 = Vertex("v7")
    v8 = Vertex("v8")

    g.add_edge(v1, v2)
    g.add_edge(v3, v2)
    g.add_edge(v3, v7)
    g.add_edge(v5, v6, 3)
    g.add_edge(v7, v2, 3)
    g.add_edge(v4, v5)
    g.add_edge(v5, v8)
    g.add_edge(v5, v3, 4)
    g.add_edge(v8, v3)
    g.add_edge(v4, v6, 2)
    g.add_edge(v7, v5, 2)

    # assert g.get_adj(v2) == [v1, v3, v7]
    # assert g.get_adj(v5) == [v6, v4, v8, v7]
    # assert g.get_weight(v5, v7) == 3
    # assert g.get_weight(v7, v5) == 3

    h = HeuristicGraph(g)
    ai = a.ASolver(g, v6, h.get_h_val)
    if ai.find_shortest_path():
        print(ai.get_shortest_path())
        print(ai.get_weight_sp())
        print(ai.get_f_score_sp())
    else:
        print("no path")

    # open_set = dpq.MinDictPQ()
    # open_set.insert((2,v3))
    # open_set.insert((2,v7))

test_1()
