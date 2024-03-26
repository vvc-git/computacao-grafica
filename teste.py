import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF

class Viewport(QGraphicsView):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.setStyleSheet("background-color: white;")  # Define a cor de fundo da viewport

        self.setSceneRect(QRectF(self.viewport().rect()))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setSceneRect(QRectF(self.viewport().rect()))

class Window(QGraphicsView):
    def __init__(self, viewport):
        super().__init__()
        self.setViewport(viewport)
        self.setStyleSheet("background-color: lightgray;")  # Define a cor de fundo da window

        self.setScene(QGraphicsScene())
        self.setRenderHint(QPainter.Antialiasing)  # Melhora a qualidade do desenho

    def drawEllipse(self, x, y, width, height):
        self.scene().addEllipse(x, y, width, height)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo Window e Viewport")
        self.setGeometry(100, 100, 600, 400)

        # Criando a viewport e a window
        self.viewport = Viewport(self)
        self.window = Window(self.viewport)

        # Definindo a window como a central
        self.setCentralWidget(self.window)

        # Adicionando um item à window (será nossa "viewport")
        self.window.drawEllipse(0, 0, 100, 100)

    def keyPressEvent(self, event):
        # Movimenta a janela para mostrar apenas metade da elipse
        if event.key() == Qt.Key_Left:
            self.moveWindow(-10, 0)
        elif event.key() == Qt.Key_Right:
            self.moveWindow(10, 0)
        elif event.key() == Qt.Key_Up:
            self.moveWindow(0, -10)
        elif event.key() == Qt.Key_Down:
            self.moveWindow(0, 10)

    def moveWindow(self, dx, dy):
        self.window.move(dx, dy)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
