from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from object import Point


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Point('ponto1', (1, 2))
    window.show()
    sys.exit(app.exec_())
