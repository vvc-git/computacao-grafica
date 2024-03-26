from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame

from utils.constant import WINDOW_HEIGHT, WINDOW_WIDTH
from ui.gui import Ui_MainWindow
from core.viewport import Viewport

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.wireframe import Wireframe

from ui.addLineDialog import AddLineDialog
from ui.addPointDialog import AddPointDialog
from ui.addRectangleDialog import AddRectangleDialog
from ui.addWireframeDialog import AddWireframeDialog

from core.world import World


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configura a interface gráfica
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Cria uma lista para armazenar os objetos a serem desenhados
        self._display_file = []

        # Define os widgets principais
        self._main = self._ui.centralWidget
        self._terminal = self._ui.terminalWidget
        self._options = self._ui.optionsWidget
        
        self._world = World(100,100)


        self._viewport = Viewport(self, self._world, parent=self)
        self._world.set_viewport(self._viewport)

        # Define widgets relacionados aos tipos de objetos
        self._types_objects = self._ui.typesListWidget
        self._types_add_button = self._ui.typesAddButton

        # Define widgets relacionados aos objetos
        self._objects = self._ui.objectsListWidget
        self._objects_remove_button = self._ui.objectsRemoveButton

        # Define widget relacionados ao movimento
        self._up_button = self._ui.upButton
        self._down_button = self._ui.downButton
        self._left_button = self._ui.leftButton
        self._right_button = self._ui.rightButton

        # Define widget relacionados ao zoom
        self._zoom_slider = self.ui.zoomHorizontalSlider


        # Conecta os ações da janela
        self.actions_connection()


    # Métodos getters para os atributos privados
    @property
    def ui(self):
        return self._ui


    @property
    def main(self):
        return self._main


    @property
    def viewport(self):
        return self._viewport


    @property
    def terminal(self):
        return self._terminal


    @property
    def options(self):
        return self._options


    @property
    def types_objects(self):
        return self._types_objects


    @property
    def types_add_button(self):
        return self._types_add_button


    @property
    def objects(self):
        return self._objects


    @property
    def objects_remove_button(self):
        return self._objects_remove_button


    @property
    def up_button(self):
        return self._up_button
    

    @property
    def down_button(self):
        return self._down_button
    
    
    @property
    def left_button(self):
        return self._left_button
    

    @property
    def right_button(self):
        return self._right_button
    

    @property
    def zoom_slider(self):
        return self._zoom_slider
    

    @property
    def display_file(self):
        return self._display_file


    def setup_viewport(self):
        # Configura a área de visualização do terminal
        self.terminal.setStyleSheet("background-color: white;")


    def actions_connection(self):
        # Conecta as ações da janela aos respectivos métodos

        # Botão de adicionar novo objeto gráfico
        self.types_add_button.clicked.connect(self.on_types_add_button)
        
        # Botão de remover objeto gráfico
        self.objects_remove_button.clicked.connect(self.on_objects_remove_button)

        # Deslocamento
        self.left_button.clicked.connect(self._world.shift_left)
        self.right_button.clicked.connect(self._world.shift_right)
        self.up_button.clicked.connect(self._world.shift_up)
        self.down_button.clicked.connect(self._world.shift_down)

        # Slider de zoom
        self.zoom_slider.valueChanged.connect(self.on_zoom_slider)
    

    def on_types_add_button(self):
        # Abre o diálogo correspondente ao tipo de objeto selecionado
        selectedType = self.types_objects.currentItem().text()
        if selectedType == "Point":
            self.open_add_point_dialog()
        elif selectedType == "Line":
            self.open_add_line_dialog()
        elif selectedType == "Rectangle":
            self.open_add_rectangle_dialog()
        elif selectedType == "Wireframe":
            self.open_add_wireframe_dialog()
        else:
            raise ValueError("The selected type is invalid.")


    def on_objects_remove_button(self):
        selected_shapes = self.objects.selectedItems()
        
        for shape in selected_shapes:
            row = self.objects.row(shape)
            del self.viewport.shapes[row]
            self.objects.takeItem(row)


    def on_zoom_slider(self):
        self.ui.update_zoom_label_text(self.zoom_slider.value())
    
    def add_objects_list(self, shape):
        self._world._display_file.append(shape)
        self._world.update_visible()
        self.viewport.shapes.append(shape)
        self.objects.addItem(shape.name)
        self.update()


    # Métodos para abrir os diálogos de adição de objetos
    def open_add_point_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = AddPointDialog()
        ui.setupUi(dialog)
        
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            x_value = ui.get_x_value()
            y_value = ui.get_y_value()
            
            point = Point(x_value, y_value, "Point")
            self.add_objects_list(point)
        


    def open_add_line_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = AddLineDialog()
        ui.setupUi(dialog)
        
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            start_point = (ui.get_x1_value(), ui.get_y1_value())
            end_point = (ui.get_x2_value(), ui.get_y2_value())

            line = Line(start_point, end_point, "Line")
            self.add_objects_list(line)


    def open_add_rectangle_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = AddRectangleDialog()
        ui.setupUi(dialog)
       
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            start_point = (ui.get_x_value(), ui.get_y_value())
            width = ui.get_width_value()
            height = ui.get_height_value()

            rectangle = Rectangle(start_point, width, height, "Rectangle")
            self.add_objects_list(rectangle)


    def open_add_wireframe_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = AddWireframeDialog()
        ui.setupUi(dialog)
        
        ui.addButton.clicked.connect(ui.add_item)
        ui.removeButton.clicked.connect(ui.remove_item)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            points = ui.get_points_value()

            wireframe = Wireframe(points, "Wireframe")
            self.add_objects_list(wireframe)
            
    def paintEvent(self, event):
      painter = QPainter(self)
      transformed_shapes = self._world.get_transformed_shapes((self._viewport._bottom_left.x(),
                                                                       self._viewport._bottom_left.y(),
                                                                       self._viewport._up_right.x(),
                                                                       self._viewport._up_right.y()))

      for shape, transformed_coords in transformed_shapes:
          shape.draw(painter, transformed_coords)