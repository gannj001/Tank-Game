__author__ = 'John'

import sfml as sf

from Turret import TankTurret
from Shell import Shell


class AssaultGunTurret(TankTurret):
    def __init__(self, texture):
        TankTurret.__init__(self, texture)
        print "Assault Gun Turret Initialised"

    def change_facing(self, mouse_position):
        self.rotation = self.tank.rotation

    def fire(self):
        if self.ready_to_fire:
            self.ready_to_fire = False
            self.count = 0
            s = Shell((sf.Texture.from_file("res/Shell.png")))
            s.setup(self, self.get_forward_point())
            self.shells.append(s)
            self.shells_fired += 1
