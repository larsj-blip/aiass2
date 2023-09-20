import json
from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    x: int
    y: int

    def move(self, x_displacement, y_displacement):
        self.x += x_displacement
        self.y += y_displacement

    def to_list(self) -> List[int]:
        return [self.x, self.y]

    def to_string(self) -> str:
        return json.dumps({"x":self.x, "y":self.y})

    @staticmethod
    def from_string(json_string: str):
        dict_with_values = json.loads(json_string)
        return (Coordinate(dict_with_values["x"],dict_with_values["y"]))
