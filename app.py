from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from object import Point
from window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec_())