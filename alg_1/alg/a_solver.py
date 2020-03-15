""" A* search algorithm implementation. It is class whats only purpose
    is to find the sortest path in graph. Graph on the input should be instance
    of Graph class.
"""
from alg import graph as gr
from typing import Callable
from alg import dict_pq as dpq

class ASolver:
    """ A* search algorithm """

    def __init__(self, graph: gr.Graph, h: Callable):
        """ Initializes the solver instance 

            Parameters:
            graph: graph instance to be search
            h: heuristic function used to search the path in graph
               Input value of function is vertex, return value is cost 
               as a number.

            Returns:
            None
        """
        first_vertex = graph.getFirstVertex()
        self._graph = graph

        # already discovered nodes. Initialized with first vertex.
        # Each vertex is stored in pririty queue as tuple (priority, vertex)
        self._open_set = dpq.MinDictPQ()
        self._open_set.insert((0, first_vertex)) 

        # for node n, cameFrom[n] is the node immediately preceding it 
        # on the cheapest path from start to n currently known.
        # Node is supposed to be grapth vetrex
        self.came_from = {}

        # g_score[n] is cost of the cheapest path from start to node n
        # known so far. Initially set to 0 for first vertex.
        self.g_score = {first_vertex: 0}
        self.f_score = self.g_score[first_vertex] + h(first_vertex)

    def findShortestPath(self) -> None:
        """ Finds shortest path in the given graph

            Parameters:
            None

            Returns:
            None
        """
        while not self._open_set.getSize():
            currentVertex = self._open_set.getMin()[1]
            # get all neighbours and add them into priority queue
            self._graph.get_adj(currentVertex)

         