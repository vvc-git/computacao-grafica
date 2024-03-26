from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from object import Line
from PyQt5.QtWidgets import QMainWindow
from constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X
from pyDialogs.addLineDialog import AddLineDialog
from pyDialogs.addPointDialog import AddPointDialog
from pyDialogs.addRectangleDialog import AddRectangleDialog
from pyDialogs.addWireframeDialog import AddWireframeDialog


class Window(QMainWindow):  
  def __init__(self):
    super().__init__()
    # configurando MainWindow
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

    # setando widget principal
    self.main = self.ui.centralWidget

    # setando widgets do grid
    self.viewport = Viewport(self.ui.viewportWidget)
    self.terminal = self.ui.terminalWidget
    self.options = self.ui.optionsWidget
    
    # setando widgets relacionados aos tipos de objetos
    self.typesObjects = self.ui.typesListWidget
    self.typesAddButton = self.ui.typesAddButton

    # setando widgets relacionados aos objetos
    self.objects = self.ui.objectsListWidget
    self.objectsRemoveButton = self.ui.objectsRemoveButton

    # realizando conexões dos botões da window
    self.buttonsConnection()

    self.display_file = []
    self.teste()


    # !! APAGAR
  def teste(self):
    # Adicione quantos objetos gráficos você quiser aqui
    objeto = Line('Line k ', [(500, 0), (600, 200)], QPen(Qt.red, 1.5), self.viewport)  # 5 é a largura da linha)

    self.display_file.append(objeto)


  def setUpViewport(self):
    self.terminal.setStyleSheet("background-color: white;")


  def setUpMenu1(self):
    painter = QPainter(self)
    painter.setBrush(QColor(200,200,200))
    painter.drawRect(self.mapToGlobal(self.horizontalLayoutWidget.pos()).x(), self.mapToGlobal(self.horizontalLayoutWidget.pos()).y(), self.horizontalLayoutWidget.width(), self.horizontalLayoutWidget.height())


  # Função reimplementada da QMaindWindow
  # é chamado automaticamente pelo sistema de event loop do Qt sempre que a janela precisar ser redesenhada.
  def paintEvent(self, event):
    self.setUpViewport()
    painter = QPainter(self)

    for objeto in self.display_file:
      objeto.draw(painter)

  def buttonsConnection(self):
    self.ui.typesAddButton.clicked.connect(self.typesObjectsButtonsConnection)


  def typesObjectsButtonsConnection(self):
    selectedType = self.typesObjects.currentItem().text()

    if selectedType == "Point":
      self.openAddPointDialog()
    elif selectedType == "Line":
      self.openAddLineDialog()
    elif selectedType == "Rectangle":
      self.openAddRectangleDialog()
    elif selectedType == "Wireframe":
      self.openAddWireframeDialog()
    else:
      print("O tipo selecionado é inválido.")


  def openAddPointDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = AddPointDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()


  def openAddLineDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = AddLineDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()


  def openAddRectangleDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = AddRectangleDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()


  def openAddWireframeDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = AddWireframeDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()

  # Classe reimplementada da QMaindWindow
  # é chamado automaticamente pelo sistema de event loop do Qt sempre que a janela precisar ser redesenhada.
  # def paintEvent(self, a0: QPaintEvent | None) -> None:
  #   # self.setUpMenu1()
  #   # self.setUpViewport()
  #   # self.setUpMenu2()
  #   p1 = Point('p1', (1, 2))
  #   p1g = GraphicalPoint(p1, self)

class Viewport(QWidget):  
  def __init__(self, viewport_ui): #points = (x1, y1)
    super().__init__()
    self.widget = viewport_ui
    self.limitX = WINDOW_WIDTH - VIEWPORT_WIDTH
    self.limitY = WINDOW_HEIGHT - VIEWPORT_HEIGHT
    self.x = WINDOW_WIDTH - VIEWPORT_WIDTH
    self.y = WINDOW_HEIGHT - VIEWPORT_HEIGHT

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def getLimitX(self):
    return self.x

  def getLimitY(self):
    return self.y

  def desloca(self):
    self.x -= 200