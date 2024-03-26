import uuid
from abc import ABC, abstractmethod
from typing import List, Tuple

from PyQt5.QtGui import QColor

from shapes.shapeType import ShapeType


class AbstractShape(ABC):
    def __init__(self, points: List[Tuple[int, int]], name: str, color: QColor):
        self._points = points
        self._id: uuid.UUID = uuid.uuid4()
        self._name: str = name
        self._color: str = color
        self._type = ShapeType.OTHERS


    @property
    def points(self) -> List[Tuple[int, int]]:
        return self._points


    @points.setter
    def points(self, value: List[Tuple[int, int]]):
        self._points = value


    @property
    def id(self) -> uuid.UUID:
        return self._id


    @id.setter
    def id(self, value: uuid.UUID):
        self._id = value


    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, value: str):
        self._name = value


    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value: QColor):
        self._color = value
    
    
    @property
    def type(self) -> ShapeType:
        return self._type


    @type.setter
    def type(self, value: ShapeType):
        self._type = value


    @abstractmethod
    def draw(self):
        pass
