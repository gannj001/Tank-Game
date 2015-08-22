__author__ = 'John'

import sfml as sf


class Nondestroyable(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(self, texture)
        self.position = None
        self.collided = False
        self.health = 10
        self.resist = 0
        self.rect = self.global_bounds

    def set_position(self, position):
        self.position = position

    def update(self, shells):
        pass
