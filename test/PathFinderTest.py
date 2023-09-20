from assertpy import assert_that

from src.Map import MapObj
from src.PathFinder import PathFinder, Coordinate


class AStarTest:

    @staticmethod
    def should_find_goal_node_task_1():
        path_finder = AStarTest.initialize_pathfinder(1)
        path_finder.run()
        path_finder.draw_path()
        assert_that(path_finder.solution_path).contains(path_finder.get_goal_position().to_string())

    @staticmethod
    def should_find_goal_node_task_2():
        path_finder = AStarTest.initialize_pathfinder(2)
        path_finder.run()
        path_finder.draw_path()
        assert_that(path_finder.solution_path).contains(path_finder.get_goal_position().to_string())

    @staticmethod
    def should_find_goal_node_task_3():
        path_finder = AStarTest.initialize_pathfinder(task=3)
        path_finder.run()
        path_finder.draw_path()
        assert_that(path_finder.solution_path).contains(path_finder.get_goal_position().to_string())
    @staticmethod
    def should_find_goal_node_task_4():
        path_finder = AStarTest.initialize_pathfinder(task=4)
        path_finder.run()
        path_finder.draw_path()
        assert_that(path_finder.solution_path).contains(path_finder.get_goal_position().to_string())
    @staticmethod
    def create_task_1_starting_coordinate():
        return Coordinate(x=27, y=18)

    @staticmethod
    def initialize_pathfinder(task:int):
        samf_map = MapObj(task=task)
        path_finder = PathFinder(samf_map, task=task)
        return path_finder
