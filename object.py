from abc import ABC, abstractmethod
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

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


class Point(QWidget):
    def __init__(self, name, points): #points = (x1, y1)
        super().__init__()
        self.points = points
        self.name = name
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Desenhar Ponto')

    def paintEvent(self, event):
        painter = QPainter()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # Desenha o ponto no centro da janela
        painter.drawPoint(self.width() // 2, self.height() // 2)