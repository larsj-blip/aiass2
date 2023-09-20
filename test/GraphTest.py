import unittest

import numpy
from assertpy import assert_that

from src.BasicGraph import BasicGraph
from src.Map import MapObj


class BasicGraphTest:


    @staticmethod
    def should_create_graph_from_multidimensional_array():
        task_map = MapObj().int_map
        graph = BasicGraph(task_map)
        assert_that(graph.vertices).is_length(len(graph.edges))

    # what should the graph do? the graph should contain nodes and edges between nodes.
    # should be able to generate graph from map
    # should by default have cost between edges be uniform cost
    # should get neighbors to node

