__author__ = 'John'

import sfml as sf

from workarounds import point_rect_intersect


class Button(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(self, texture)
        self.position = None
        self.clicked = False

    def set_position(self, position):
        self.position = position

    def check_clicked(self, mouse_position):
        if point_rect_intersect(mouse_position, self.global_bounds):
            self.clicked = True

    def update(self, mouse_position):
        self.check_clicked(mouse_position)
