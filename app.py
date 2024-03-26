from PyQt5 import QtWidgets
import sys
from core.window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec_())           