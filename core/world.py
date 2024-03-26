from typing import List, Tuple
from PyQt5.QtCore import QPointF
from core.viewport import Viewport
from shapes.abstractShape import AbstractShape

class World:
    def __init__(self, main_window, display_file: List[AbstractShape]):
        self._main_window = main_window
        self._display_file = display_file

        self._bottom_left = QPointF(-100, -100)
        self._up_right = QPointF(100, 100)

    def set_viewport(self, viewport: Viewport):
        self.viewport = viewport

    def get_transformed_shapes(self, viewport_geometry: Tuple[float, float, float, float]) -> List[Tuple[AbstractShape, Tuple[int, int]]]:
        transformed_shapes = []
        for shape in self._display_file:
            transformed_coords = [self.to_viewport(coord, viewport_geometry) for coord in shape._points]
            transformed_shapes.append((shape, transformed_coords))
        return transformed_shapes
    
    def to_viewport(self, coord: Tuple[int, int], viewport_geometry: Tuple[float, float, float, float]) -> Tuple[int]:
        (xvmin, yvmin, xvmax, yvmax) = viewport_geometry
        xwmax, ywmax, xwmin, ywmin = self._up_right.x(), self._up_right.y(), self._bottom_left.x(), self._bottom_left.y()

        xw, yw = int(coord[0]), int(coord[1])
        
        multx = xvmax - xvmin 
        multy = yvmax - yvmin
        xvp = xvmin + (xw - xwmin) / (xwmax - xwmin) * multx
        yvp = yvmin + (1 - (yw - ywmin) / (ywmax - ywmin)) * multy

        return (int(xvp), int(yvp))
    
    def shift_left(self) -> None:
        xnew = self._bottom_left.x() + 10
        self._bottom_left.setX(xnew)

        xnew = self._up_right.x() + 10
        self._up_right.setX(xnew)
        self._main_window.update()
        print('botao esquerdo')
    
    def shift_right(self)-> None:
        xnew = self._bottom_left.x() - 10
        self._bottom_left.setX(xnew)

        xnew = self._up_right.x() - 10
        self._up_right.setX(xnew)

        self._main_window.update()
        print('botao direito')

    def shift_up(self) -> None:
        ynew = self._bottom_left.y() - 10
        self._bottom_left.setY(ynew)

        ynew = self._up_right.y() - 10
        self._up_right.setY(ynew)

        self._main_window.update()
        print('botao cima')
    
    def shift_down(self) -> None:
        ynew = self._bottom_left.y() + 10
        self._bottom_left.setY(ynew)

        ynew = self._up_right.y() + 10
        self._up_right.setY(ynew)

        self._main_window.update()
        print('botao baixo')

    def zoom_in(self) -> None:
        self._bottom_left.setX(self._bottom_left.x() + 10)
        self._bottom_left.setY(self._bottom_left.y() + 10)

        self._up_right.setX(self._up_right.x() - 10)
        self._up_right.setY(self._up_right.y() - 10)

        self._main_window.update()
        print('zoom')

    