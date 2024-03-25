from abc import ABC, abstractmethod
from PyQt5.QtCore import Qt, QLineF, QRect
from PyQt5.QtGui import QPen
from constant import WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X



class Object(ABC):
    @abstractmethod
    def __init__(self):
        self.id = None
        self.name = None
        self.color = None
        self.points = []
        self.viewport = None

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
    def __init__(self, name, points, color, viewport):
        self.x = points[0][0]
        self.y = points[0][1]
        self.color = color
        self.viewport = viewport

    def draw(self, painter):
        # * Teoricamente isso, funciona, mas os pontos são muito pequenos 
        # painter.setBrush(QBrush(self.cor))
        # painter.drawPoint(self.x, self.y)
        # painter.drawRect(self.x, self.y, 150, 150)

        # * Isso gera circulos bem pequenos para representar os pontos
        # Define o tamanho do ponto
        tamanho_ponto = 10

        posicaoX = self.x + self.viewport.getX() 
        posicaoY = VIEWPORT_HEIGHT - self.y

        # Calcula o retângulo que circunda o ponto
        x_esquerda = posicaoX - tamanho_ponto // 2
        y_superior = self.y - tamanho_ponto // 2

        ponto_rect = QRect(posicaoX, posicaoY, tamanho_ponto, tamanho_ponto)
        # Desenha o círculo centrado no ponto
        painter.drawEllipse(ponto_rect)


class Line(Object):
    def __init__(self, name, points, color, viewport):
        self.name = name
        self.points = points
        self.color =  color
        self.viewport = viewport

    def verifica_limites(self, point):
        if (point[0] < WINDOW_WIDTH - VIEWPORT_WIDTH):
            print('esta a esquerda', point)
            intersec = self.find_intersection_point(point, (300,400), (WINDOW_WIDTH - VIEWPORT_WIDTH,0), (WINDOW_WIDTH - VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
            print('ponto encontrado adicionado:', intersec)
            return intersec
        else:
            return point
    
    def find_intersection_point(self, line1_start, line1_end, line2_start, line2_end):
        x1, y1 = line1_start[0], line1_start[1]
        x2, y2 = line1_end[0], line1_end[1]
        x3, y3 = line2_start[0], line2_start[1]
        x4, y4 = line2_end[0], line2_end[1]

        # Calcula as coordenadas de interseção
        denominator = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        if denominator == 0:  # As linhas são paralelas ou coincidentes
            return None
        else:
            px = (((x1 * y2 - y1 * x2) * (x3 - x4)) - ((x1 - x2) * (x3 * y4 - y3 * x4))) / denominator
            py = (((x1 * y2 - y1 * x2) * (y3 - y4)) - ((y1 - y2) * (x3 * y4 - y3 * x4))) / denominator
            return (int(px), int(py))

    def draw(self, painter):

        Point1 = self.points[0]
        Point2 = self.points[1]
        
        # Corrige em relação ao viewport
        posicaoX1 = Point1[0] + self.viewport.getX()
        posicaoY1 = VIEWPORT_HEIGHT - Point1[1]

        point = self.verifica_limites((posicaoX1, posicaoY1))

        posicaoX2 = Point2[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoY2 = VIEWPORT_HEIGHT - Point2[1]

        # Desenha o círculo centrado no ponto
        painter.setPen(self.color)
        # painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)
        painter.drawLine(point[0], point[1], posicaoX2, posicaoY2)

# Polígono
class Wireframe(Object):
    def __init__(self, name, points, color, viewport):
        self.name = name
        self.points = points
        self.color =  color
        self.viewport = viewport

    def draw(self, painter):

        first = previous = self.points[0] 

        for i, point in enumerate(self.points):
    
            if i > 0:
            
                # Corrige em relação ao viewport
                posicaoX1 = previous[0] + self.viewport.getX() 
                posicaoY1 = VIEWPORT_HEIGHT - previous[1]
                posicaoX2 = point[0] + self.viewport.getX() 
                posicaoY2 = VIEWPORT_HEIGHT - point[1] 

                # Desenha o círculo centrado no ponto
                painter.setPen(self.color)
                painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)

                previous = point

                if i == (len(self.points)-1):
                    # Corrige em relação ao viewport
                    posicaoLastX = point[0] + self.viewport.getX() 
                    posicaoLastY = VIEWPORT_HEIGHT - point[1] 
                    posicaoFirstX = first[0] + self.viewport.getX()
                    posicaoFirstY = VIEWPORT_HEIGHT - first[1]

                    # Desenha o círculo centrado no ponto
                    painter.setPen(self.color)
                    painter.drawLine(posicaoLastX, posicaoLastY, posicaoFirstX, posicaoFirstY)


            


        #if (point[0] > VIEWPORT_WIDTH):
        #    print('esta a direita')
        #if (point[1] < 0):
        #    print('esta a acima')
        #if (point[1] > VIEWPORT_HEIGHT):
        #    print('esta a abaixo')
        


                



