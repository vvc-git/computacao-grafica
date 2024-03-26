
from PyQt5.QtCore import QPointF

class World:
    def __init__(self, main_window, display_file):
        # hardcoded por enquanto
        self.x = 100;
        self.y = 100;
        self.width = 1000;
        self.height = 1000;
        self._main_window = main_window
        self._display_file = display_file

        self.__bottom_left = QPointF(-100, -100)
        self.__up_right = QPointF(100, 100)

    def set_viewport(self, viewport):
        self._viewport = viewport

    def get_transformed_shapes(self, viewport_geometry):
        transformed_shapes = []
        for shape in self._display_file:
            transformed_coords = self.transform_shape(shape, viewport_geometry)
            transformed_shapes.append((shape, transformed_coords))
        return transformed_shapes
    
    def transform_shape(self, shape, viewport_geometry):
      return [self.to_viewport(coord, viewport_geometry) for coord in shape.points]
    
    def to_viewport(self, coord, viewport_geometry):
        (xvmin, yvmin, xvmax, yvmax) = viewport_geometry
        xwmax, ywmax, xwmin, ywmin = self.__up_right.x(), self.__up_right.y(), self.__bottom_left.x(), self.__bottom_left.y()

        xw, yw = coord.x(), coord.y()
        
        multx = xvmax - xvmin 
        multy = yvmax - yvmin
        xvp = xvmin + (xw - xwmin) / (xwmax - xwmin) * multx
        yvp = yvmin + (1 - (yw - ywmin) / (ywmax - ywmin)) * multy

        return (int(xvp), int(yvp))
    
    def shift_left(self):
        xnew = self.__bottom_left.x() + 50
        self.__bottom_left.setX(xnew)

        xnew = self.__up_right.x() + 50
        self.__up_right.setX(xnew)
        self._main_window.update_paint_event()
        print('botao esquerdo')
    
    def shift_right(self):
        xnew = self.__bottom_left.x() - 50
        self.__bottom_left.setX(xnew)

        xnew = self.__up_right.x() - 50
        self.__up_right.setX(xnew)

        self._main_window.update_paint_event()
        print('botao direito')

    def shift_up(self):
        ynew = self.__bottom_left.y() - 50
        self.__bottom_left.setY(ynew)

        ynew = self.__up_right.y() - 50
        self.__up_right.setY(ynew)

        self._main_window.update_paint_event()
        print('botao cima')
    
    def shift_down(self):
        ynew = self.__bottom_left.y() + 50
        self.__bottom_left.setY(ynew)

        ynew = self.__up_right.y() + 50
        self.__up_right.setY(ynew)

        self._main_window.update_paint_event()
        print('botao baixo')

    