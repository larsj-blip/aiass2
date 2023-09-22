import json
from dataclasses import dataclass, field
from typing import List

from numpy import ndarray

from src.Coordinate import Coordinate


@dataclass
class BasicGraph:
    map_as_multidimension_array: ndarray
    vertices: dict = field(default_factory=lambda: {})
    edges: dict = field(default_factory=lambda: {})

    def __post_init__(self):
        self.construct_graph()

    def get_cost(self, position):
        pass

    def construct_graph(self):
        self.map_size = (len(self.map_as_multidimension_array, ), len(self.map_as_multidimension_array[0]))
        for x_index, row in enumerate(self.map_as_multidimension_array):
            for y_index, element in enumerate(row):
                vertex = Vertex(element, Coordinate(x_index, y_index))
                if vertex.is_walkable():
                    self.add_vertex_to_hashmap_of_vertices(vertex)
                    self.add_valid_neighbors_to_hashmap_of_edges(vertex)

    def add_valid_neighbors_to_hashmap_of_edges(self, vertex):
        self.edges[vertex.location.to_string()] = self.get_valid_neighbors_within_the_map(vertex.location,
                                                                                          self.map_as_multidimension_array)

    def add_vertex_to_hashmap_of_vertices(self, vertex):
        self.vertices[vertex.location.to_string()] = vertex

    def get_valid_neighbors_within_the_map(self, location: Coordinate, samf_map) -> List[str]:
        valid_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        neighbors = []
        for move in valid_moves:
            x_coordinate = location.x - move[0]
            y_coordinate = location.y - move[1]
            if self.is_within_x_coordinate_boundary(x_coordinate):
                if self.is_within_y_coordinate_boundary(y_coordinate):
                    if Vertex(samf_map[x_coordinate][y_coordinate],
                              Coordinate(x_coordinate, y_coordinate)).is_walkable():
                        neighbors.append(Coordinate(x_coordinate, y_coordinate).to_string())
        return neighbors

    def is_within_y_coordinate_boundary(self, y_coordinate):
        return 0 <= y_coordinate <= self.map_size[1] - 1

    def is_within_x_coordinate_boundary(self, x_coordinate):
        return 0 <= x_coordinate <= self.map_size[0] - 1

    def get_neighbors(self, position: Coordinate) -> List[str]:
        return self.edges[position.to_string()]


@dataclass
class GraphWithUnifomCost(BasicGraph):

    def get_cost(self, position):
        return 1


@dataclass
class GraphWithVariableCost(BasicGraph):

    def get_cost(self, destination_position) -> int:
        vertex = self.vertices[destination_position]
        return vertex.vertex_type


@dataclass
class Vertex:
    vertex_type: int
    location: Coordinate

    def is_walkable(self) -> bool:
        if self.vertex_type == -1:
            return False
        elif self.vertex_type >= 1:
            return True

    def to_string(self):
        location_string = self.location.to_string()
        vertex_type_string = str(self.vertex_type)
        return json.dumps({"location": location_string, "vertex_type": vertex_type_string})
