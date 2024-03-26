from typing import List, Tuple

from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape


class Wireframe(AbstractShape):
    def __init__(self, points: List[Tuple[int, int]], name: str, color: QColor = QColor(255, 0, 0)):
        super().__init__(points, name, color)
        self._type = ShapeType.WIREFRAME


    def draw(self):
        print("Drawing a wireframe with points:")
        for i, (x, y) in enumerate(self.points):
            print(f"Point {i+1}: ({x}, {y})")
