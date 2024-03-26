from typing import List, Tuple

from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape


class Wireframe(AbstractShape):
    def __init__(self, points: List[Tuple[int, int]], name: str, color: QColor = QColor(255, 0, 0)):
        super().__init__(points, name, color)
        self._type = ShapeType.WIREFRAME


    def draw(self, painter, points):
        print("Drawing a wireframe with points:")
        painter.setPen(self.color)
        (xf, yf) = (xp, yp)  = points[0]
        print((xf, yf))


        for i, (x, y) in enumerate(points):
            if i > 0:
                painter.drawLine(xp, yp, x, y)

                if  i == (len(self.points)-1):
                    painter.drawLine(x, y, xf, yf)
           
