from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from object import Point
from GraphicalObject import GraphicalPoint, ObjetoGrafico
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):  
    def __init__(self): #points = (x1, y1)
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.viewport = self.ui.Viewport
      self.verticalLayoutWidget = self.ui.MenuDeFuncoes
      self.horizontalLayoutWidget = self.ui.Terminal
      self.objetos_graficos = []
      self.criar_objetos_graficos()

    def criar_objetos_graficos(self):
        # Adicione quantos objetos gráficos você quiser aqui
        objeto1 = Point(50, 50, QColor(0, 0, 0))  # Quadrado preto
        objeto2 = Point(200, 200, QColor(255, 0, 0))  # Quadrado vermelho

        self.objetos_graficos.append(objeto1)
        self.objetos_graficos.append(objeto2)

    def setUpViewport(self):
      painter = QPainter(self)
      painter.setBrush(QColor(120,120,120))
      painter.drawRect(self.mapToGlobal(self.viewport.pos()).x(), self.mapToGlobal(self.viewport.pos()).y(), self.viewport.width(), self.viewport.height())

    def setUpMenu1(self):
      painter = QPainter(self)
      painter.setBrush(QColor(200,200,200))
      painter.drawRect(self.mapToGlobal(self.horizontalLayoutWidget.pos()).x(), self.mapToGlobal(self.horizontalLayoutWidget.pos()).y(), self.horizontalLayoutWidget.width(), self.horizontalLayoutWidget.height())

    def setUpMenu2(self):
      painter = QPainter(self)
      painter.setBrush(QColor(58,58,58))
      painter.drawRect(self.mapToGlobal(self.verticalLayoutWidget.pos()).x(), self.mapToGlobal(self.verticalLayoutWidget.pos()).y(), self.verticalLayoutWidget.width(), self.verticalLayoutWidget.height())

    

    # Classe reimplementada da QMaindWindow
    # é chamado automaticamente pelo sistema de event loop do Qt sempre que a janela precisar ser redesenhada.
    # def paintEvent(self, a0: QPaintEvent | None) -> None:
    #   # self.setUpMenu1()
    #   # self.setUpViewport()
    #   # self.setUpMenu2()
    #   p1 = Point('p1', (1, 2))
    #   p1g = GraphicalPoint(p1, self)
      
    def paintEvent(self, event):
      painter = QPainter(self)
      for objeto in self.objetos_graficos:
          objeto.desenhar(painter)


       