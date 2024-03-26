from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import QRect

from shapes.shapeType import ShapeType
from shapes.abstractShape import AbstractShape
from utils.constant import DEFAULT_SHAPE_COLOR


class Point(AbstractShape):
    def __init__(self, x: int, y: int, name: str, color: QColor = DEFAULT_SHAPE_COLOR):
        super().__init__([(x, y)], name, color)
        self._type = ShapeType.POINT

    def draw(self, painter, points):
        x, y = points[0]
        #painter.setPen(self.color)
        #painter.setBrush(QBrush(self.color))
        #painter.drawPoint(x, y)

        # * Isso gera circulos bem pequenos para representar os pontos
        tamanho_ponto = 10

        # Calcula o retângulo que circunda o ponto
        x_esquerda = x - tamanho_ponto // 2
        y_superior = y - tamanho_ponto // 2

        # Define o tamanho do ponto
        ponto_rect = QRect(x_esquerda, y_superior, tamanho_ponto, tamanho_ponto)
        
        # Desenha o círculo centrado no ponto
        painter.drawEllipse(ponto_rect)


        print(f"Drawing a point at ({x}, {y})")
