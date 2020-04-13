""" A* search algorithm implementation. It is class whats only purpose
    is to find the sortest path in graph. Graph on the input should be instance
    of Graph class.
"""
from alg import graph as gr
from typing import Callable
from alg import dict_pq as dpq
import math


class ASolver:
    """ A* search algorithm """

    def __init__(self, graph: gr.Graph, goal, h: Callable):
        """ Initializes the solver instance. Shortest path is found
            from first vertex of graph to the goal. 

            Parameters:
            graph: graph instance to be search
            goal: goal we are finding the shortest path to
            h: heuristic function used to search the path in graph
               Input value of function is vertex, return value is cost 
               as a number.

            Returns:
            None
        """
        first_vertex = graph.get_first_vertex()
        self._graph: gr.Graph = graph
        self._goal = goal
        self._h_func: Callable = h

        # already discovered nodes. Initialized with first vertex.
        # Each vertex is stored in pririty queue as tuple (priority, vertex)
        self._open_set = dpq.MinDictPQ()
        self._open_set.insert((0, first_vertex))

        # List of nodes already discovered and explored.
        # Starts off empty
        # Once a node has been 'current' it then goes here
        self._close_set = []

        # for node n, cameFrom[n] is the node immediately preceding it
        # on the cheapest path from start to n currently known.
        # Node is supposed to be grapth vetrex
        self._came_from = {}

        # g_score[n] is cost of the cheapest path from start to node n
        # known so far. Initially set to 0 for first vertex.
        self._g_score = {first_vertex: 0}
        self._f_score = {first_vertex: 0}

    def find_shortest_path(self) -> None:
        """ Finds shortest path in the given graph from the first vertex of the graph to the goal.

            Parameters:
            None

            Returns:
            True if path is found, False if there is not path between first vertex anf goal
        """
        ret_val = False
        while self._open_set.getSize() > 0:
            # Get current vertex from the priority queue
            curr_h_score, current_vertex = self._open_set.getMin()
            curr_g_score = self._g_score[current_vertex]

            if current_vertex == self._goal:
                ret_val = True
                break

            self._close_set.append(current_vertex)

            # get all neighbours, check if better path is not found
            # and add them into priority queue if new path is better
            for vertex in self._graph.get_adj(current_vertex):
                if vertex not in self._close_set:
                    new_g_score = curr_g_score + \
                        self._graph.get_weight(vertex, current_vertex)
                    g_score = self._g_score.get(vertex, math.inf)
                    # if new score is better than current score -> add vertex
                    # into priority queue under better calclulated score
                    if new_g_score < g_score:
                        new_f_score = new_g_score + \
                            self._h_func(current_vertex, vertex)
                        self._g_score[vertex] = new_g_score
                        self._f_score[vertex] = new_f_score
                        self._came_from[vertex] = current_vertex
                        try:
                            self._open_set.insert((new_f_score, vertex))
                        except KeyError:
                            self._open_set.changePriority(
                                (new_f_score, vertex))

        return ret_val

    def get_shortest_path(self) -> list:
        """ Returns found shortest path as a list of vertices

            Parameters:
            None

            Returns:
            list of vertices representing shortest path
        """
        curr_vertex = self._goal
        ret_val = [curr_vertex]
        while curr_vertex:
            curr_vertex = self._came_from.get(curr_vertex)
            if curr_vertex:
                ret_val.append(curr_vertex)
        ret_val.reverse()
        return ret_val

    def get_weight_sp(self) -> float:
        """ Returns weight of the shortest path

            Parameters:
            None

            Returns:
            weight of the shortest path 
        """
        return self._g_score.get(self._goal)

    def get_f_score_sp(self) -> float:
        """ Returns f score of the shortest path

            Parameters:
            None

            Returns:
            f score of the shortest path 
        """
        return self._f_score.get(self._goal)