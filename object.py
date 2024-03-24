from abc import ABC, abstractmethod
from PyQt5.QtCore import Qt, QLineF, QRect
from PyQt5.QtGui import QPen
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
    def __init__(self, name, points, color):
        self.x = points[0][0]
        self.y = points[0][1]
        self.color = color

    def draw(self, painter):
        # * Teoricamente isso, funciona, mas os pontos são muito pequenos 
        # painter.setBrush(QBrush(self.cor))
        # painter.drawPoint(self.x, self.y)
        # painter.drawRect(self.x, self.y, 150, 150)

        # * Isso gera circulos bem pequenos para representar os pontos
        # Define o tamanho do ponto
        tamanho_ponto = 10

        posicaoX = self.x + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoY = VIEWPORT_HEIGHT - self.y

        # Calcula o retângulo que circunda o ponto
        x_esquerda = posicaoX - tamanho_ponto // 2
        y_superior = self.y - tamanho_ponto // 2

        ponto_rect = QRect(posicaoX, posicaoY, tamanho_ponto, tamanho_ponto)
        # Desenha o círculo centrado no ponto
        painter.drawEllipse(ponto_rect)


class Line(Object):
    def __init__(self, name, points, color):
        self.name = name
        self.points = points
        self.color =  color

    def draw(self, painter):

        Point1 = self.points[0]
        Point2 = self.points[1]
        
        # Corrige em relação ao viewport
        posicaoX1 = Point1[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoY1 = VIEWPORT_HEIGHT - Point1[1]

        posicaoX2 = Point2[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoY2 = VIEWPORT_HEIGHT - Point2[1]

        # Desenha o círculo centrado no ponto
        painter.setPen(self.color)
        painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)

# Polígono
class Wireframe(Object):
    def __init__(self, name, points, color):
        self.name = name
        self.points = points
        self.color =  color

    def draw(self, painter):

        first = previous = self.points[0] 

        for i, point in enumerate(self.points):
    
            if i > 0:
            
                # Corrige em relação ao viewport
                posicaoX1 = previous[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
                posicaoY1 = VIEWPORT_HEIGHT - previous[1]

                posicaoX2 = point[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
                posicaoY2 = VIEWPORT_HEIGHT - point[1]

                # Desenha o círculo centrado no ponto
                painter.setPen(self.color)
                painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)

                previous = point

                if i == (len(self.points)-1):
                    # Corrige em relação ao viewport
                    posicaoLastX = point[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
                    posicaoLastY = VIEWPORT_HEIGHT - point[1]

                    posicaoFirstX = first[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
                    posicaoFirstY = VIEWPORT_HEIGHT - first[1]

                    # Desenha o círculo centrado no ponto
                    painter.setPen(self.color)
                    painter.drawLine(posicaoLastX, posicaoLastY, posicaoFirstX, posicaoFirstY)





                



