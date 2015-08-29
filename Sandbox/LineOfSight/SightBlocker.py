__author__ = 'John'

import sfml as sf


class SightBlocker(sf.RectangleShape):
    def __init__(self, size):
        sf.RectangleShape.__init__(self, size)
        self.position = None
        self.outline_color = sf.Color.RED
        self.outline_thickness = 5
        self.blocks_sight = True

    def set_position(self, position):
        self.position = position
