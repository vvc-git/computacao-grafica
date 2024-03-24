from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from object import Point, Line, Wireframe
from PyQt5.QtWidgets import QApplication, QMainWindow
from constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X

class Window(QMainWindow):  
    def __init__(self): #points = (x1, y1)
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.viewport = Viewport(self.ui.viewportWidget)
      self.verticalLayoutWidget = self.ui.functionsMenuWidget
      self.horizontalLayoutWidget = self.ui.terminalWidget
      self.display_file = []
      self.setWindowTitle('Computação Gráfica 2D')
      self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
      self.teste()
      self.teste2()

    # !! APAGAR
    def teste(self):
        # Adicione quantos objetos gráficos você quiser aqui
        objeto1 = Point('Point 1', [(0, 0)], QPen(Qt.green, 1.5), self.viewport)  
        objeto2 = Line('Line X ', [(0, 0), (VIEWPORT_WIDTH, 0)], QPen(Qt.red, 1.5))  # 5 é a largura da linha)
        objeto3 = Line('Line Y ', [(0, 0), (0, VIEWPORT_HEIGHT)], QPen(Qt.red, 1.5))  # 5 é a largura da linha)
        objeto4 = Wireframe('Triangulo', [(0,0), (300, 0), (300, 400), (350, 500)], QPen(Qt.blue, 1.5), self.viewport)

        self.display_file.append(objeto2)
        self.display_file.append(objeto1)
        self.display_file.append(objeto3)
        self.display_file.append(objeto4)
    
    def teste2(self):
      self.viewport.desloca()

    def setUpViewport(self):
      self.viewport.setStyleSheet("background-color: gray;")

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
      


class Viewport():  
    def __init__(self, viewport_ui): #points = (x1, y1)
      self.widget = viewport_ui
      self.limitX = WINDOW_WIDTH - VIEWPORT_WIDTH
      self.limitY = WINDOW_HEIGHT - VIEWPORT_HEIGHT
      self.x = WINDOW_WIDTH - VIEWPORT_WIDTH
      self.y = WINDOW_HEIGHT - VIEWPORT_HEIGHT

    def getX(self):
       return self.x
    
    def getY(self):
      return self.y
    
    def getLimitX(self):
       return self.x
    
    def getLimitY(self):
      return self.y

    def desloca(self):
       self.x -= 100




       