
from PyQt5.QtCore import QPointF

class World:
    def __init__(self, main_window, display_file):
        self.main_window = main_window
        self.display_file = display_file

        self.bottom_left = QPointF(-100, -100)
        self.up_right = QPointF(100, 100)

    def set_viewport(self, viewport):
        self.viewport = viewport

    def get_transformed_shapes(self, viewport_geometry):
        transformed_shapes = []
        for shape in self.display_file:
            transformed_coords = [self.to_viewport(coord, viewport_geometry) for coord in shape.points]
            transformed_shapes.append((shape, transformed_coords))
        return transformed_shapes
    
    def to_viewport(self, coord, viewport_geometry):
        (xvmin, yvmin, xvmax, yvmax) = viewport_geometry
        xwmax, ywmax, xwmin, ywmin = self.up_right.x(), self.up_right.y(), self.bottom_left.x(), self.bottom_left.y()

        xw, yw = coord.x(), coord.y()
        
        multx = xvmax - xvmin 
        multy = yvmax - yvmin
        xvp = xvmin + (xw - xwmin) / (xwmax - xwmin) * multx
        yvp = yvmin + (1 - (yw - ywmin) / (ywmax - ywmin)) * multy

        return (int(xvp), int(yvp))
    
    def shift_left(self):
        xnew = self.bottom_left.x() + 10
        self.bottom_left.setX(xnew)

        xnew = self.up_right.x() + 10
        self.up_right.setX(xnew)
        self.main_window.update()
        print('botao esquerdo')
    
    def shift_right(self):
        xnew = self.bottom_left.x() - 10
        self.bottom_left.setX(xnew)

        xnew = self.up_right.x() - 10
        self.up_right.setX(xnew)

        self.main_window.update()
        print('botao direito')

    def shift_up(self):
        ynew = self.bottom_left.y() - 10
        self.bottom_left.setY(ynew)

        ynew = self.up_right.y() - 10
        self.up_right.setY(ynew)

        self.main_window.update()
        print('botao cima')
    
    def shift_down(self):
        ynew = self.bottom_left.y() + 10
        self.bottom_left.setY(ynew)

        ynew = self.up_right.y() + 10
        self.up_right.setY(ynew)

        self.main_window.update()
        print('botao baixo')

    def zoom_in(self):
        self.bottom_left.setX(self.bottom_left.x() + 10)
        self.bottom_left.setY(self.bottom_left.y() + 10)

        self.up_right.setX(self.up_right.x() - 10)
        self.up_right.setY(self.up_right.y() - 10)

        self.main_window.update()
        print('zoom')

    