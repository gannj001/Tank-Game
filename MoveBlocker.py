__author__ = 'John'

import sfml as sf


class MoveBlocker(sf.RectangleShape):
    def __init__(self, size):
        sf.RectangleShape.__init__(self, size)
        self.position = None
        self.origin = self.local_bounds.center
        self.outline_color = sf.Color.RED
        self.outline_thickness = 5
        self.blocks_sight = True
        self.blocks_movement = True

    def set_position(self, position):
        self.position = position
