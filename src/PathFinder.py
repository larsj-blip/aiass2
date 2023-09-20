from dataclasses import dataclass

from Map import MapObj


@dataclass
class PathFinder:
    map: MapObj
    def take_step(self):
        return True



