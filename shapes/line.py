from typing import Tuple

from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape


class Line(AbstractShape):
    def __init__(self, start_point: Tuple[int, int], end_point: Tuple[int, int], name: str, color: QColor = QColor(255, 0, 0)):
        super().__init__([start_point, end_point], name, color)
        self._type = ShapeType.LINE


    def draw(self, painter, points):
        start_x, start_y = points[0]
        end_x, end_y = points[1]
        painter.setPen(self.color)
        painter.drawLine(start_x, start_y, end_x, end_y)

    
    def get_points(self):
        return self._points