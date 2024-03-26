from typing import Tuple

from shapeType import ShapeType
from abstractShape import AbstractShape


class Line(AbstractShape):
    def __init__(self, start_point: Tuple[int, int], end_point: Tuple[int, int], shape_id: int, name: str, color: str):
        super().__init__([start_point, end_point], shape_id, name, color)
        self._type = ShapeType.LINE


    def draw(self):
        start_x, start_y = self.points[0]
        end_x, end_y = self.points[1]
        print(f"Drawing a line from ({start_x}, {start_y}) to ({end_x}, {end_y})")
