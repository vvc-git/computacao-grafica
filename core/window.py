from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow

from utils.constant import WINDOW_HEIGHT, WINDOW_WIDTH
from ui.gui import Ui_MainWindow
from object import Line
from core.viewport import Viewport

from ui.addLineDialog import AddLineDialog
from ui.addPointDialog import AddPointDialog
from ui.addRectangleDialog import AddRectangleDialog
from ui.addWireframeDialog import AddWireframeDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configura a interface gráfica
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Define os widgets principais
        self._main = self._ui.centralWidget
        self._viewport = Viewport(self._ui.viewportWidget)
        self._terminal = self._ui.terminalWidget
        self._options = self._ui.optionsWidget

        # Define widgets relacionados aos tipos de objetos
        self._types_objects = self._ui.typesListWidget
        self._types_add_button = self._ui.typesAddButton

        # Define widgets relacionados aos objetos
        self._objects = self._ui.objectsListWidget
        self._objects_remove_button = self._ui.objectsRemoveButton

        # Cria uma lista para armazenar os objetos a serem desenhados
        self._display_file = []

        # Conecta os botões da janela
        self._buttons_connection()

        # Adiciona objetos gráficos para teste
        self._teste()


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
    def display_file(self):
        return self._display_file
    
    
    def _teste(self):
        # Adiciona um objeto do tipo Line para teste
        objeto = Line('Line k', [(500, 0), (600, 200)], QPen(Qt.red, 1.5), self.viewport)
        self.display_file.append(objeto)


    def paintEvent(self, event):
        # Redesenha a janela
        self._set_up_viewport()
        painter = QPainter(self)
        for objeto in self.display_file:
            objeto.draw(painter)


    def _set_up_viewport(self):
        # Configura a área de visualização do terminal
        self.terminal.setStyleSheet("background-color: white;")


    def _buttons_connection(self):
        # Conecta os botões da janela aos respectivos métodos
        self.types_add_button.clicked.connect(self._types_objects_buttons_connection)


    def _types_objects_buttons_connection(self):
        # Abre o diálogo correspondente ao tipo de objeto selecionado
        selectedType = self.types_objects.currentItem().text()
        if selectedType == "Point":
            self._open_add_point_dialog()
        elif selectedType == "Line":
            self._open_add_line_dialog()
        elif selectedType == "Rectangle":
            self._open_add_rectangle_dialog()
        elif selectedType == "Wireframe":
            self._open_add_wireframe_dialog()
        else:
            raise ValueError("The selected type is invalid.")


    # Métodos para abrir os diálogos de adição de objetos
    def _open_add_point_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = AddPointDialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def _open_add_line_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = AddLineDialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def _open_add_rectangle_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = AddRectangleDialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def _open_add_wireframe_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = AddWireframeDialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
