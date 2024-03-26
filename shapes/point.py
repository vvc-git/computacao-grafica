from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape


class Point(AbstractShape):
    def __init__(self, x: int, y: int, name: str, color: QColor = QColor(255, 0, 0)):
        super().__init__([(x, y)], name, color)
        self._type = ShapeType.POINT


    def draw(self):
        x, y = self.points[0]
        print(f"Drawing a point at ({x}, {y})")
