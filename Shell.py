__author__ = 'John'

import math

import sfml as sf


class Shell(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(self, texture)
        self.speed = 10
        self.lifetime = 30
        self.age = 0
        self.turret = None
        self.target = None
        self.dead = False
        self.damage = 10

    def setup(self, turret, target):
        self.set_turret(turret)
        self.set_position()
        self.set_target(target)
        self.set_rotation()

    def set_turret(self, turret):
        self.turret = turret

    def set_position(self):
        self.position = self.turret.position

    def set_target(self, mouse_position):
        self.target = mouse_position

    def set_rotation(self):
        dx = self.target.x - self.position.x
        dy = self.target.y - self.position.y
        angle = math.degrees(math.atan2(dy, dx)) + 90
        self.rotation = angle

    def move(self):
        x = math.sin(math.radians(self.rotation)) * self.speed
        y = math.cos(math.radians(self.rotation)) * -self.speed
        self.position += (x, y)

    def check_life(self):
        if self.age >= self.lifetime:
            self.dead = True

    def update(self):
        self.check_life()
        self.move()

        self.age += 1
