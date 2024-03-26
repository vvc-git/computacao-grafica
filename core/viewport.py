from typing import List

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

from shapes.abstractShape import AbstractShape
from utils.constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, DEFAULT_SHAPE_COLOR

from core.window import Window
from shapes.point import Point
from shapes.line import Line


class Viewport(QWidget):  
    def __init__(self, x_min: int, y_min: int, x_max: int, y_max: int, window: Window, parent = None):
        super().__init__(parent)

        # Definindo ponto minimo e maximo da viewport
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        
        # Definindo parte do mundo que é visível
        self._window = window


    @property
    def x_min(self) -> int:
        return self._x_min


    @property
    def y_min(self) -> int:
        return self._y_min


    @property
    def x_max(self) -> int:
        return self._x_max
  

    @property
    def y_max(self) -> int:
        return self._y_max


    @property
    def window(self) -> int:
        return self._window


    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)

        # Configura propriedades de desenho
         # Cor azul e espessura de linha 2
        painter.setPen(QPen(Qt.blue, 2)) 

        # Desenha elementos no widget
        painter.fillRect(self.rect(), QColor(255, 255, 0))  # Fundo amarelo
        painter.drawText(self.rect(), "Olá, PyQt!", alignment=Qt.AlignCenter)  # Texto centralizado
        painter.drawRect(50, 50, 200, 100)  # Desenha um retângulo nas coordenadas (50, 50) com largura 200 e altura 100
        painter.drawLine(50, 50, 250, 150)  # Desenha uma linha de (50, 50) até (250, 150)








    # def desloca(self):
    #     # Verifica se o deslocamento não ultrapassa os limites
    #     if self._x - 200 >= 0:
    #         self._x -= 200
    #     else:
    #         self._x = 0

    #     if self._y - 200 >= 0:
    #         self._y -= 200
    #     else:
    #         self._y = 0


    # def paintEvent(self, event):
    #   painter = QPainter(self)
    #   painter.setPen(QPen(Qt.white, 10, Qt.SolidLine))
    #   painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
    #   transformed_shapes = self._world.get_transformed_shapes((self._bottom_left.x(),
    #                                                                    self._bottom_left.y(),
    #                                                                    self._up_right.x(),
    #                                                                    self._up_right.y()))

    #   for shape, transformed_coords in transformed_shapes:
    #       shape.draw(painter, transformed_coords)