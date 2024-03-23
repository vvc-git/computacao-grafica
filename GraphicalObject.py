from object import Point
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QPainter, QColor, QBrush


class GraphicalPoint(QWidget):
    def __init__(self, ponto: Point, MainWindow):
        super().__init__()
        self.ponto = ponto
        self.main = MainWindow

#     def paintEvent(self, event):
#         painter = QPainter(self.main)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
#         # Desenha o ponto no centro da janela
#         painter.drawPoint(self.width() // 2, self.height() // 2)

class ObjetoGrafico:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def desenhar(self, painter):
        painter.setBrush(QBrush(self.cor))
        painter.drawPoint()
        painter.drawRect(self.x, self.y, self.largura, self.altura)

    