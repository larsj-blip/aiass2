from assertpy import assert_that

from Map import MapObj
from src.PathFinder import PathFinder


def shouldTakeSingleStepTowardsGoal():
    map = MapObj()
    path_finder = PathFinder(map)
