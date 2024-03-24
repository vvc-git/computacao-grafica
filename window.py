from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from object import Point
from PyQt5.QtWidgets import QApplication, QMainWindow
from constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH

class Window(QMainWindow):  
    def __init__(self): #points = (x1, y1)
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.viewport = self.ui.Viewport
      self.verticalLayoutWidget = self.ui.MenuDeFuncoes
      self.horizontalLayoutWidget = self.ui.Terminal
      self.display_file = []
      self.setWindowTitle('Computação Gráfica 2D')
      self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
      self.teste()

    # !! APAGAR
    def teste(self):
        # Adicione quantos objetos gráficos você quiser aqui
        objeto1 = Point(50, 50, QColor(0, 0, 0))  # Quadrado preto
        objeto2 = Point(200, 200, QColor(255, 0, 0))  # Quadrado vermelho

        self.display_file.append(objeto1)
        self.display_file.append(objeto2)

    def setUpViewport(self):
      painter = QPainter(self)
      painter.setBrush(QColor(120,120,120))
      painter.drawRect(WINDOW_WIDTH-VIEWPORT_WIDTH, 0, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

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

    
    # Função reimplementada da QMaindWindow
    # é chamado automaticamente pelo sistema de event loop do Qt sempre que a janela precisar ser redesenhada.
    def paintEvent(self, event):
      self.setUpViewport()
      painter = QPainter(self)
      for objeto in self.display_file:
          objeto.draw(painter)


       