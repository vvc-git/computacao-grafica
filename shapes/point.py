from shapeType import ShapeType
from abstractShape import AbstractShape


class Point(AbstractShape):
    def __init__(self, x: int, y: int, shape_id: int, name: str, color: str):
        super().__init__([(x, y)], shape_id, name, color)
        self._type = ShapeType.POINT


    def draw(self):
        x, y = self.points[0]
        print(f"Drawing a point at ({x}, {y})")
