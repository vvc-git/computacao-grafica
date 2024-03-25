from PyQt5.QtWidgets import QMainWindow
from addWireframeDialog import Ui_AddWireframeDialog

class AddWireframe(object):  
    def __init__(self):
      super().__init__()
      self.ui = Ui_AddWireframeDialog()
      self.ui.setupUi(self)