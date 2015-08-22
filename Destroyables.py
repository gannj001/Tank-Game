__author__ = 'John'

import sfml as sf

from workarounds import intersects


class Destroyable(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(self, texture)
        self.position = None
        self.collided = None
        self.health = 10
        self.resist = 0
        self.rect = self.global_bounds
        self.alive = True

    def set_position(self, position):
        self.position = position

    def check_collision(self, shells):
        for shell in shells:
            if intersects(self.global_bounds, shell.global_bounds):
                print "collision"
                return shell

    def check_alive(self):
        if self.health <= 0:
            self.alive = False

    def update(self, shells):
        self.collided = self.check_collision(shells)
        if self.collided:
            shells.remove(self.collided)


class StationaryTarget(Destroyable):
    def __init__(self, texture):
        Destroyable.__init__(self, texture)
        self.h = 15
        self.w = 16

    def take_damage(self):
        self.health -= self.collided.damage - self.resist

    def update(self, shells):
        super(StationaryTarget, self).update(shells)
        if self.collided:
            self.take_damage()
        self.collided = None
        self.check_alive()
