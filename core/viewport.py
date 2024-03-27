from typing import List

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

from shapes.abstractShape import AbstractShape
from utils.constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH

from shapes.point import Point
from shapes.line import Line


class Viewport(QWidget):  
    def __init__(self, world, parent=None):
        super().__init__(parent)

        self._world = world
        self._parent = parent

        # self._widget = viewport_ui
        self._limitX = WINDOW_WIDTH - VIEWPORT_WIDTH
        self._limitY = WINDOW_HEIGHT - VIEWPORT_HEIGHT
        self._x = self._limitX
        self._y = self._limitY
        self._shapes = []

        self._bottom_left = QPointF(0, 540)
        self._up_right = QPointF(50, 4300)

    @property
    def shapes(self) -> List[AbstractShape]:
        return self._shapes


    @shapes.setter
    def shapes(self, value: List[AbstractShape]):
        self._shapes = value


    @property
    def limitX(self):
        return self._limitX


    @property
    def limitY(self):
        return self._limitY


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


    def desloca(self):
        # Verifica se o deslocamento não ultrapassa os limites
        if self._x - 200 >= 0:
            self._x -= 200
        else:
            self._x = 0

        if self._y - 200 >= 0:
            self._y -= 200
        else:
            self._y = 0

    def paintEvent(self, event):
        print('viewport paint Event')
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 10, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        transformed_shapes = self._world.get_transformed_shapes((self._bottom_left.x(),
                                                                        self._bottom_left.y(),
                                                                        self._up_right.x(),
                                                                        self._up_right.y()))

        
        for shape, transformed_coords in transformed_shapes:
            print(shape)
            shape.draw(painter, transformed_coords)
        
        painter.end()
