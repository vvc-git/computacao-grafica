from designer import Ui_MainWindow

class Window(Ui_MainWindow):  
    def __init__(self, MainWindow): #points = (x1, y1)
      super().__init__()
      ui = Ui_MainWindow()
      ui.setupUi(MainWindow)