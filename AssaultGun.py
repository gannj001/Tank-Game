__author__ = 'John'

from Tank import TankBody


class AssaultGunBody(TankBody):
    def __init__(self, texture):
        TankBody.__init__(self, texture)
        self.traverse = 2
        print "Assault Gun Initialised"
