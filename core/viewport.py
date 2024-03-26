from typing import List

from PyQt5.QtWidgets import QWidget

from shapes.abstractShape import AbstractShape
from utils.constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH


class Viewport(QWidget):  
    def __init__(self, viewport_ui):
        super().__init__()
        self._widget = viewport_ui
        self._limitX = WINDOW_WIDTH - VIEWPORT_WIDTH
        self._limitY = WINDOW_HEIGHT - VIEWPORT_HEIGHT
        self._x = self._limitX
        self._y = self._limitY
        self._shapes: List[AbstractShape] = []


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
