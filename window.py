from designer import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor

class Window(Ui_MainWindow):  
    def __init__(self, MainWindow): #points = (x1, y1)
      super().__init__()
      ui = Ui_MainWindow()
      ui.setupUi(MainWindow)
      viewportX = ui.Viewport.width()
      viewportY = ui.centralwidget.height()

    def paintEvent(self, x, y):
        painter = QPainter()
        painter.setPen(QColor())  # Define a cor da borda do retângulo
        painter.setBrush(QColor(0, 0, 255, 100))  # Define a cor do preenchimento do retângulo
        painter.drawRect(50, 50, x, y)  # Desenha um retângulo nas coordenadas (50, 50) com largura 200 e altura 100
        painter.end()