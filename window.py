from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QPointF
from object import Point, Line, Wireframe
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from constant import WINDOW_HEIGHT, WINDOW_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_X, VIEWPORT_GEOMETRY, VIEW_FRAME_GEOMETRY
from world import World
from viewport import Viewport
from PyQt5 import QtWidgets as wdg

class Window(QMainWindow):  
    def __init__(self): #points = (x1, y1)
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.display_file = []

      # Create World window
      self.world = World(self, self.display_file)

      # Create Viewport
      # ! TESTE
      view_frame = self.__build_frame(self, VIEW_FRAME_GEOMETRY)
      self.__view_frame = view_frame
      self.viewport = Viewport(self, self.world, parent=self.__view_frame)
      self.viewport.setGeometry(VIEWPORT_GEOMETRY)
      
      self.world.set_viewport(self.viewport)
      self.setWindowTitle('Computação Gráfica 2D')
      self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

      # Deslocamento
      self.ui.leftButton.clicked.connect(self.world.shift_left)
      self.ui.rightButton.clicked.connect(self.world.shift_right)
      self.ui.upButton.clicked.connect(self.world.shift_up)
      self.ui.downButton.clicked.connect(self.world.shift_down)

      # Zoom 
      self.ui.zoomHorizontalSlider.setMinimum(50)
      self.ui.zoomHorizontalSlider.setMaximum(200)
      self.ui.zoomHorizontalSlider.setValue(100)
      self.ui.zoomHorizontalSlider.setTickInterval(10)
      self.ui.zoomHorizontalSlider.setTickPosition(QSlider.TicksBelow)
      self.ui.zoomHorizontalSlider.valueChanged.connect(self.updateZoom)

      self.teste()

    # !! APAGAR
    def teste(self):
      # Adicione quantos objetos gráficos você quiser aqui
      objeto1 = Point('Point 1', [QPointF(0, -100)], QPen(Qt.green, 1.5), self.viewport) 

      objeto4 = Line('Line x ', [QPointF(0, self.viewport._bottom_left.y()), QPointF(0,0)], QPen(Qt.red, 1.5), self.viewport)  # 5 é a largura da linha)
      objeto5 = Line('Line y ', [QPointF(0, 0), QPointF(100, 200)], QPen(Qt.red, 1.5), self.viewport) 

      self.display_file.append(objeto1)
      self.display_file.append(objeto5)
      print('teste foi chamado')
      self.update
  
    def paintEvent(self, event):
      # self.setUpViewport()
      painter = QPainter(self)
      transformed_shapes = self.world.get_transformed_shapes((self.viewport._bottom_left.x(),
                                                                       self.viewport._bottom_left.y(),
                                                                       self.viewport._up_right.x(),
                                                                       self.viewport._up_right.y()))

      for shape, transformed_coords in transformed_shapes:
          shape.draw(painter, transformed_coords)

    def __build_frame(self, parent: wdg.QWidget, geometry: tuple[int]) -> wdg.QFrame:
        frame = wdg.QFrame(parent)
        frame.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        frame.setFrameStyle(wdg.QFrame.WinPanel | wdg.QFrame.Plain)
        return frame 
    
    def update_paint_event(self):
        # Atualiza o paintEvent
        self.update()
        
    def updateZoom(self, value):
        # Atualiza o valor exibido no QLabel com o valor do slider
        self.ui.zoomLabel.setText("Zoom: {}%".format(value))
      
        print(value)
        # Chamada para a função que aplica o zoom com base no valor do slider
        # Substitua esta chamada pela sua função de aplicação de zoom
        self.world.zoom_in()
      
    
       
       
      




       