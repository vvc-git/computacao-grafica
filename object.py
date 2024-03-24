from abc import ABC, abstractmethod
from PyQt5.QtCore import Qt, QLineF, QRect
from constant import WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH



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

        posicaoX = self.x + WINDOW_WIDTH - VIEWPORT_WIDTH
        print(posicaoX)

        # Calcula o retângulo que circunda o ponto
        x_esquerda = posicaoX - tamanho_ponto // 2
        y_superior = self.y - tamanho_ponto // 2

        ponto_rect = QRect(posicaoX, y_superior, tamanho_ponto, tamanho_ponto)
        # Desenha o círculo centrado no ponto
        painter.drawEllipse(ponto_rect)


class Line(Object):
    def __init__(self, x1, y1, x2, y2, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor = cor

    def draw(self, painter):
        # * Teoricamente isso, funciona, mas os pontos são muito pequenos 
        # painter.setBrush(QBrush(self.cor))
        # painter.drawPoint(self.x, self.y)
        # painter.drawRect(self.x, self.y, 150, 150)

        # * Isso gera circulos bem pequenos para representar os pontos
        posicaoX1 = self.x1 + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoX2 = self.x2 + WINDOW_WIDTH - VIEWPORT_WIDTH

        # Desenha o círculo centrado no ponto
        painter.drawLine(posicaoX1, self.y1, posicaoX2, self.y2)
