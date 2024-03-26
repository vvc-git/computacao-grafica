from typing import Tuple

from shapeType import ShapeType
from abstractShape import AbstractShape


class Rectangle(AbstractShape):
    def __init__(self, bottom_left: Tuple[int, int], width: int, height: int, shape_id: int, name: str, color: str):
        super().__init__([], shape_id, name, color)
        self._bottom_left = bottom_left
        self._width = width
        self._height = height
        self._calculate_points()
        self._type = ShapeType.RECTANGLE 


    @property
    def bottom_left(self) -> Tuple[int, int]:
        return self._bottom_left


    @bottom_left.setter
    def bottom_left(self, value: Tuple[int, int]):
        self._bottom_left = value
        self._calculate_points()


    @property
    def bottom_right(self) -> Tuple[int, int]:
        return self._bottom_right


    @bottom_right.setter
    def bottom_right(self, value: Tuple[int, int]):
        self._bottom_right = value
        # Atualizar o ponto inferior esquerdo
        self._bottom_left = (value[0] - self._width, value[1])


    @property
    def top_left(self) -> Tuple[int, int]:
        return self._top_left


    @top_left.setter
    def top_left(self, value: Tuple[int, int]):
        self._top_left = value
        # Atualizar o ponto inferior esquerdo
        self._bottom_left = (value[0], value[1] - self._height)


    @property
    def top_right(self) -> Tuple[int, int]:
        return self._top_right


    @top_right.setter
    def top_right(self, value: Tuple[int, int]):
        self._top_right = value
        # Atualizar o ponto inferior esquerdo
        self._bottom_left = (value[0] - self._width, value[1] - self._height)


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
        x, y = self._bottom_left
        self._bottom_right = (x + self._width, y)
        self._top_left = (x, y + self._height)
        self._top_right = (x + self._width, y + self._height)


    def draw(self):
        bottom_left_x, bottom_left_y = self.bottom_left
        top_right_x, top_right_y = self._top_right
        bottom_right_x, bottom_right_y = self._bottom_right
        top_left_x, top_left_y = self._top_left
        
        width = self._width
        height = self._height

        print(f"Bottom Right: ({bottom_left_x}, {bottom_left_y})")
        print(f"Top Right: ({top_right_x}, {top_right_y})")
        print(f"Bottom Right: ({bottom_right_x}, {bottom_right_y})")
        print(f"Top Left: ({top_left_x}, {top_left_y})")
        print(f"Dimensions: {width} x {height})")

