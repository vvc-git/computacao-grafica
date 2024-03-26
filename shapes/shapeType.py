from enum import Enum, auto

class ShapeType(Enum):
    POINT = auto()
    LINE = auto()
    RECTANGLE = auto()
    WIREFRAME = auto()
    OTHERS = auto()