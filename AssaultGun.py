__author__ = 'John'

import math

import sfml as sf

from Tank import TankBody
from Turret import TankTurret
from Shell import Shell


class AssaultGun(TankBody, TankTurret):
    def __init__(self, texture):
        TankBody.__init__(self, texture)
        TankTurret.__init__(self, texture)

    def change_facing(self, mouse_position):
        pass

    def fire(self):
        x = math.sin(math.radians(self.rotation)) * 10
        y = math.cos(math.radians(self.rotation)) * 10
        target = (x, y)
        if self.ready_to_fire:
            self.ready_to_fire = False
            self.count = 0
            s = Shell((sf.Texture.from_file("res/Shell.png")))
            s.setup(self, target)
            self.shells.append(s)
            self.shells_fired += 1

    def update(self, mouse, window, keyboard):
        super(TankBody, self).update(self, mouse, window, keyboard)
