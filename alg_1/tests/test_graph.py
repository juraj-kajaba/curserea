import pytest
from alg import graph as gr
from functools import total_ordering


@total_ordering
class Vertex:
    """ Auxialiary class for testing purpose 
        Must be comparable, because if first priority in compared tuples are equal 
    """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name 

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.name < other.name 

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
    g.add_edge(v5, v6)
    g.add_edge(v7, v2)
    g.add_edge(v4, v5)
    g.add_edge(v5, v8)
    g.add_edge(v7, v5, 3)

    assert g.get_adj(v2) == [v1, v3, v7]
    assert g.get_adj(v5) == [v6, v4, v8, v7]
    assert g.get_weight(v5, v7) == 3
    assert g.get_weight(v7, v5) == 3


test_1()
