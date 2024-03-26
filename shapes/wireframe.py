from typing import List, Tuple

from shapeType import ShapeType
from abstractShape import AbstractShape


class Wireframe(AbstractShape):
    def __init__(self, points: List[Tuple[int, int]], shape_id: int, name: str, color: str):
        super().__init__(points, shape_id, name, color)
        self._type = ShapeType.WIREFRAME


    def draw(self):
        print("Drawing a wireframe with points:")
        for i, (x, y) in enumerate(self.points):
            print(f"Point {i+1}: ({x}, {y})")
