from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPointF 

from PyQt5.QtCore import Qt
from object import Point, Line


class Viewport(QWidget):  
    def __init__(self, window, world, parent=None): #points = (x1, y1)
      super().__init__()
      self.window = window
      self.world = world
      self.parent = parent
      
      # self.parent.setStyleSheet("background-color: gray;")
      print(parent)
      self._bottom_left = QPointF(400, 600)
      self._up_right = QPointF(1000, 0)

      self.teste()

    # !! APAGAR
    def teste(self):
      # Adicione quantos objetos gráficos você quiser aqui
      objeto1 = Point('Point 1', [QPointF(0, -100)], QPen(Qt.green, 1.5), self) 

      objeto4 = Line('Line x ', [QPointF(0, self._bottom_left.y()), QPointF(0,0)], QPen(Qt.red, 1.5), self)  # 5 é a largura da linha)
      objeto5 = Line('Line y ', [QPointF(0, 0), QPointF(100, 200)], QPen(Qt.red, 1.5), self) 

      self.window.display_file.append(objeto1)
      self.window.display_file.append(objeto5)
      print('teste foi chamado')
      self.update
  
    def paintEvent(self, event):
      # self.setUpViewport()
      painter = QPainter(self)
      transformed_shapes = self.world.get_transformed_shapes((self._bottom_left.x(),
                                                                       self._bottom_left.y(),
                                                                       self._up_right.x(),
                                                                       self._up_right.y()))

      for shape, transformed_coords in transformed_shapes:
          shape.draw(painter, transformed_coords)