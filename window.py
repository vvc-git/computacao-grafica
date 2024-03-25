from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QPointF
from object import Point, Line, Wireframe
from PyQt5.QtWidgets import QApplication, QMainWindow
from constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X, VIEWPORT_GEOMETRY
from word import World
from viewport import Viewport

class Window(QMainWindow):  
    def __init__(self): #points = (x1, y1)
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.display_file = []

      # Create World window
      self.world = World(self, self.display_file)

      # Create Viewport
      self.viewport = Viewport(self, self.world, parent=self.ui.viewportWidget)
      self.viewport.setGeometry(VIEWPORT_GEOMETRY)
      
      self.world.set_viewport(self.viewport)
      self.setWindowTitle('Computação Gráfica 2D')
      self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
      self.teste()

    # !! APAGAR
    def teste(self):
        # Adicione quantos objetos gráficos você quiser aqui
        # objeto1 = Point('Point 1', [QPointF(0, 0)], QPen(Qt.green, 1.5), self.viewport)  
        #objeto2 = Line('Line X ', [(0, 0), (VIEWPORT_WIDTH, 0)], QPen(Qt.red, 1.5), self.viewport)  # 5 é a largura da linha)
        #objeto3 = Line('Line Y ', [(0, 0), (0, VIEWPORT_HEIGHT)], QPen(Qt.red, 1.5), self.viewport)  # 5 é a largura da linha)

        objeto4 = Line('Line x ', [QPointF(0, VIEWPORT_HEIGHT), QPointF(0,0)], QPen(Qt.red, 1.5), self.viewport)  # 5 é a largura da linha)
        objeto5 = Line('Line y ', [QPointF(0, 0), QPointF(VIEWPORT_WIDTH, 0)], QPen(Qt.red, 1.5), self.viewport) 
        #objeto4 = Wireframe('Triangulo', [(0,0), (300, 0), (300, 400), (350, 500)], QPen(Qt.blue, 1.5), self.viewport)

        #self.display_file.append(objeto1)
        # pself.display_file.append(objeto2)
        # pself.display_file.append(objeto3)
        self.display_file.append(objeto4)
        self.display_file.append(objeto5)
        #self.display_file.append(objeto4)
    
    def teste2(self):
      self.viewport.desloca()
  
    def paintEvent(self, event):
      # self.setUpViewport()
      painter = QPainter(self)
      transformed_shapes = self.world.get_transformed_shapes((self.viewport._bottom_left.x(),
                                                                       self.viewport._bottom_left.y(),
                                                                       self.viewport._up_right.x(),
                                                                       self.viewport._up_right.y()))

      for shape, transformed_coords in transformed_shapes:
          shape.draw(painter, transformed_coords) 
      
    
       
       
      




       