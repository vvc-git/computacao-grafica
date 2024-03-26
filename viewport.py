from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF

class Viewport(QWidget):  
    def __init__(self, window, world, parent=None): #points = (x1, y1)
      super().__init__()
      self.window = window
      self.world = world
      self.parent = parent
      
      # self.parent.setStyleSheet("background-color: gray;")
      print(parent)
      self._bottom_left = QPointF(0, 0)
      self._up_right = QPointF(parent.width(), parent.height())