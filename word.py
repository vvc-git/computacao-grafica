
from PyQt5.QtCore import QPointF

class World:
    def __init__(self, main_window, display_file):
        # hardcoded por enquanto
        self.x = -1000;
        self.y = -1000;
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