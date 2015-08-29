__author__ = 'John'

import sfml as sf

from Tank import TankBody
from Turret import TankTurret
from AssaultGun import AssaultGunBody
from AssaultGunTurret import AssaultGunTurret


class PlayerTank(TankBody):
    def __init__(self, texture):
        TankBody.__init__(self, texture)
        turret = TankTurret(sf.Texture.from_file("res/TankTurret.png"))
        self.set_turret(turret)
        turret.set_body(self)


class PlayerGun(AssaultGunBody):
    def __init__(self, texture):
        AssaultGunBody.__init__(self, sf.Texture.from_file("res/AssaultGunDetailed.png"))
        turret = AssaultGunTurret(sf.Texture.from_file("res/AssaultGun.png"))
        self.set_turret(turret)
        turret.set_body(self)