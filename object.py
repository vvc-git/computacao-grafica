from abc import ABC, abstractmethod
from PyQt5.QtCore import Qt, QLineF, QRect



class Object(ABC):
    @abstractmethod
    def __init__(self):
        self.id = None
        self.name = None
        self.color = None
        self.points = []

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getColor(self):
        return self.color
    
    @abstractmethod
    def draw(self):
        pass


class Point(Object):
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor

    def draw(self, painter):
        # * Teoricamente isso, funciona, mas os pontos são muito pequenos 
        # painter.setBrush(QBrush(self.cor))
        # painter.drawPoint(self.x, self.y)
        # painter.drawRect(self.x, self.y, 150, 150)

        # * Isso gera circulos bem pequenos para representar os pontos
        # Define o tamanho do ponto
        tamanho_ponto = 10

        # Calcula o retângulo que circunda o ponto
        x_esquerda = self.x - tamanho_ponto // 2
        y_superior = self.y - tamanho_ponto // 2

        ponto_rect = QRect(x_esquerda, y_superior, tamanho_ponto, tamanho_ponto)
        # Desenha o círculo centrado no ponto
        painter.drawEllipse(ponto_rect)

