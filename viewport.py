from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF

class Viewport(QLabel):  
    def __init__(self, window, world, parent=None): #points = (x1, y1)
      super().__init__()
      self.window = window
      self.world = world
      # self.widget.setStyleSheet("background-color: gray;")

      self._bottom_left = QPointF(0, 0)
      self._up_right = QPointF(440, 1150)

    def desloca(self):
       self.x -= 200