from collections import defaultdict


class Graph:
    """ Implementation of general weighted graph """

    def __init__(self):
        """ Each vertex of graph is passed as a key of dictionary
            where value is list of all adjacency vertices of the key
        """
        self._vertices = defaultdict(list)
        self._weights = {}

    def add_edge(self, vertex1, vertex2, weight: float = 1) -> None:
        """ Adds egde into graph

            Parameters:
            vertex1: first vertex of the edge
            vertex2: second vertex of the edge
            weight: weight of the edge

            Return:
            None
        """
        self._vertices[vertex1].append(vertex2)
        self._vertices[vertex2].append(vertex1)
        self._weights[(vertex1, vertex2)] = weight
        self._weights[(vertex2, vertex1)] = weight

    def get_adj(self, vertex) -> list:
        """ Returns list of all adjacent verticces

            Parameters:
            vertex: vertex whose adjacent vertices are returned

            Returns:
            list of adjacent vertices of input vertex
        """
        return self._vertices[vertex].copy()

    def get_weight(self, vertex1, vertex2) -> float:
        """ Returns the edge weight berween vertex1 and vertex2

            Parameters:
            vertex1: first vertex of the edge
            vertex2: second vertex of the edge

            Returns:
            weight of the specified edge
        """
        return self._weights[(vertex1, vertex2)]

    def get_first_vertex(self):
        """ Returns the first vertex of the graph
        """
        return next(iter(self._vertices))
