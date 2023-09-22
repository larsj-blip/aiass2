# A* algorithm based on redblobgames' implementation. Can be found at: https://www.redblobgames.com/pathfinding/a-star/implementation.py


from dataclasses import dataclass, field
from queue import PriorityQueue

from typing import List

from src.BasicGraph import BasicGraph, GraphWithUnifomCost, GraphWithVariableCost
from src.Coordinate import Coordinate
from src.Map import MapObj


@dataclass
class PathFinder:
    samf_map_helper: MapObj
    task: int = field(default=1)
    solution_path: dict = field(default_factory=lambda: {})
    solution_cost: dict = field(default_factory=lambda: {})
    samf_graph: BasicGraph = field(default=None)
    current_position: Coordinate = field(default=Coordinate(0, 0))

    def __post_init__(self):
        self.current_position = self.get_start_position()
        if self.task == 1 or self.task == 2:
            self.samf_graph = GraphWithUnifomCost(self.samf_map_helper.int_map)
        elif self.task >= 3:
            self.samf_graph = GraphWithVariableCost(self.samf_map_helper.int_map)

    def get_start_position(self) -> Coordinate:
        coordinates_as_list = self.samf_map_helper.get_start_pos()
        return self.create_coordinate_from_list(coordinates_as_list)

    def get_goal_position(self) -> Coordinate:
        coordinates_as_list = self.samf_map_helper.get_goal_pos()
        return self.create_coordinate_from_list(coordinates_as_list)

    @staticmethod
    def create_coordinate_from_list(coordinates_as_list: List[int]) -> Coordinate:
        coordinate = Coordinate(coordinates_as_list[0], coordinates_as_list[1])
        return coordinate

    def run(self):
        frontier = PriorityQueue()
        frontier.put((0, self.get_start_position().to_string()))
        accumulated_cost_for_node = {self.get_start_position().to_string(): 0}
        path_from_goal_coordinate = {self.get_start_position().to_string(): None}

        while frontier.qsize() != 0:
            current_node_coordinates = self.expand_node_with_lowest_cost(frontier)
            if current_node_coordinates == self.get_goal_position().to_string():
                break

            for neighbor_location in self.samf_graph.get_neighbors(Coordinate.from_string(current_node_coordinates)):
                cost = self.get_cost_of_moving_to_neighbor(
                    accumulated_cost_for_node, current_node_coordinates, neighbor_location)
                if not self.node_visited(accumulated_cost_for_node, neighbor_location) or self.is_shorter_path_to_node(accumulated_cost_for_node, cost, neighbor_location):
                    accumulated_cost_for_node[neighbor_location] = cost
                    frontier.put(
                        self.create_entry_in_priority_queue(cost, neighbor_location)
                    )
                    path_from_goal_coordinate[neighbor_location] = current_node_coordinates
        self.solution_path = path_from_goal_coordinate
        self.solution_cost = accumulated_cost_for_node[self.get_goal_position().to_string()]

    def expand_node_with_lowest_cost(self, frontier):
        return frontier.get()[1]

    def is_shorter_path_to_node(self, accumulated_cost_for_node, cost, neighbor_location):
        return cost < accumulated_cost_for_node[neighbor_location]

    def node_visited(self, accumulated_cost_for_node, neighbor_location):
        return neighbor_location not in accumulated_cost_for_node

    def draw_path(self):
        node = self.solution_path[self.get_goal_position().to_string()]
        while node is not None:
            coordinate = Coordinate.from_string(node).to_list()
            self.samf_map_helper.set_cell_value(coordinate, None)
            node = self.solution_path[node]
        self.samf_map_helper.show_map()

    def create_entry_in_priority_queue(self, cost, neighbor_location):
        return (self.manhattan_distance_heuristic(Coordinate.from_string(neighbor_location)) + cost, neighbor_location)

    def get_cost_of_moving_to_neighbor(self, accumulated_cost_from_start_node_to_specified_node,
                                       current_node_coordinates: str, neighbor_location: str):
        return accumulated_cost_from_start_node_to_specified_node[
            current_node_coordinates] + self.samf_graph.get_cost(neighbor_location)

    def manhattan_distance_heuristic(self, location: Coordinate) -> int:
        x_distance = abs(self.get_goal_position().x - location.x)
        y_distance = abs(self.get_goal_position().y - location.y)
        return x_distance + y_distance
