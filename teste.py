import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.rectangles = []

        # Define a cor de fundo da janela como branco
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangles(qp)
        qp.end()

    def draw_rectangles(self, qp):
        for rect in self.rectangles:
            qp.setBrush(QColor(*rect['color']))
            qp.drawRect(*rect['rectangle'])

    def generate_rectangle(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        width = random.randint(20, 200)
        height = random.randint(20, 200)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rectangles.append({'rectangle': (x, y, width, height), 'color': color})
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Gerador de Retângulos Aleatórios")

        self.central_widget = MyWidget()
        self.setCentralWidget(self.central_widget)

        self.timer = self.central_widget.startTimer(1000)  # Timer para adicionar retângulos a cada segundo

    def timerEvent(self, event):
        self.central_widget.generate_rectangle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
