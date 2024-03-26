from abc import ABC, abstractmethod
from PyQt5.QtCore import QRect
from utils.constant import WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X


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

        posicaoX = self.x + self.viewport.x 
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

    def check_limit(self, list_points):
        # Esquerda Ponto 1
        if (list_points[0][0] < WINDOW_WIDTH - VIEWPORT_WIDTH):
            print('Esquerda')
            intersec = self.find_intersection_point(list_points[0], list_points[1], (WINDOW_WIDTH - VIEWPORT_WIDTH, 0), (WINDOW_WIDTH - VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
            list_points.remove(list_points[0])
            list_points.append(intersec)
        
        # Esquerda Ponto 2
        if (list_points[1][0] < WINDOW_WIDTH - VIEWPORT_WIDTH):
            print('Esquerda')
            intersec = self.find_intersection_point(list_points[0], list_points[1], (WINDOW_WIDTH - VIEWPORT_WIDTH, 0), (WINDOW_WIDTH - VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
            list_points.remove(list_points[1])
            list_points.append(intersec)     
        
        # Direita Ponto 1
        if (list_points[0][0] > WINDOW_WIDTH):
            print('Direita')
            intersec = self.find_intersection_point(list_points[0], list_points[1], (WINDOW_WIDTH, VIEWPORT_HEIGHT), (WINDOW_WIDTH, 0))
            list_points.remove(list_points[0])
            list_points.append(intersec)   
        
        # Direita Ponto 2
        if (list_points[1][0] > WINDOW_WIDTH):
            intersec = self.find_intersection_point(list_points[0], list_points[1], (WINDOW_WIDTH, VIEWPORT_HEIGHT), (WINDOW_WIDTH, 0))
            list_points.remove(list_points[1])
            list_points.append(intersec)
        
        else:
            #print('Dentro do view')
            return False
    
        return True
    
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
        posicaoX1 = Point1[0] + self.viewport.x
        posicaoY1 = VIEWPORT_HEIGHT - Point1[1]

        posicaoX2 = Point2[0] + WINDOW_WIDTH - VIEWPORT_WIDTH
        posicaoY2 = VIEWPORT_HEIGHT - Point2[1]

        list_point = [(posicaoX1, posicaoY1), ((posicaoX2, posicaoY2))]
        point = self.check_limit(list_point)
        
        # Desenha o círculo centrado no ponto
        painter.setPen(self.color)
        if point:
            painter.drawLine(list_point[0][0], list_point[0][1], list_point[1][0], list_point[0][1])
        else:
            painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)

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
                posicaoX1 = previous[0] + self.viewport.x 
                posicaoY1 = VIEWPORT_HEIGHT - previous[1]
                posicaoX2 = point[0] + self.viewport.x 
                posicaoY2 = VIEWPORT_HEIGHT - point[1] 

                # Desenha o círculo centrado no ponto
                painter.setPen(self.color)
                painter.drawLine(posicaoX1, posicaoY1, posicaoX2, posicaoY2)

                previous = point

                if i == (len(self.points)-1):
                    # Corrige em relação ao viewport
                    posicaoLastX = point[0] + self.viewport.x 
                    posicaoLastY = VIEWPORT_HEIGHT - point[1] 
                    posicaoFirstX = first[0] + self.viewport.x
                    posicaoFirstY = VIEWPORT_HEIGHT - first[1]

                    # Desenha o círculo centrado no ponto
                    painter.setPen(self.color)
                    painter.drawLine(posicaoLastX, posicaoLastY, posicaoFirstX, posicaoFirstY)


    


                



