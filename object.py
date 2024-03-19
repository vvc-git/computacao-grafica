from abc import ABC, abstractmethod

class Object(ABC):
    @abstractmethod
    def __init__(self):
        self.id = None
        self.name = None
        self.points = []

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

    def getId(self):
        return self.id
    
    @abstractmethod
    def drawn(self, viewport):
        pass


class Point(Object):
    def __init__(self, name, points): #points = (x1, y1)
        super().__init__()
        self.points = points
        self.name = name