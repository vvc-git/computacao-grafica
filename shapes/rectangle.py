from typing import Tuple

from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape


class Rectangle(AbstractShape):
    def __init__(self, start_point: Tuple[int, int], width: int, height: int, name: str, color: QColor = QColor(255, 0, 0)):
        super().__init__([start_point], name, color)
        self._width = width
        self.height = height
        self._calculate_points()
        self._type = ShapeType.RECTANGLE 
        

    @property
    def width(self) -> int:
        return self._width


    @width.setter
    def width(self, value: int):
        self._width = value
        self._calculate_points()


    @property
    def height(self) -> int:
        return self._height


    @height.setter
    def height(self, value: int):
        self._height = value
        self._calculate_points()


    def _calculate_points(self):
        x, y = self._points[0]
        bottom_right = (x + self._width, y)
        top_right = (x + self._width, y + self._height)
        top_left = (x, y + self._height)

        self.points.append(bottom_right)
        self.points.append(top_right)
        self.points.append(top_left)


    def draw(self, painter, points):
        bottom_left_x, bottom_left_y = points[0]
        bottom_right_x, bottom_right_y = points[1]
        top_right_x, top_right_y = points[2]
        top_left_x, top_left_y = points[3]
        
        width = self._width
        height = self._height

        painter.setPen(self.color)
        painter.drawLine(bottom_left_x, bottom_left_y, bottom_right_x, bottom_right_y)
        painter.drawLine(bottom_right_x, bottom_right_y, top_right_x, top_right_y)
        painter.drawLine(top_right_x, top_right_y, top_left_x, top_left_y)
        painter.drawLine(top_left_x, top_left_y, bottom_left_x, bottom_left_y)

        print(f"Bottom Left: ({bottom_left_x}, {bottom_left_y})")
        print(f"Bottom Right: ({bottom_right_x}, {bottom_right_y})")
        print(f"Top Right: ({top_right_x}, {top_right_y})")
        print(f"Top Left: ({top_left_x}, {top_left_y})")
        print(f"Dimensions: ({width} x {height})")

