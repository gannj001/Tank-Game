__author__ = 'John'

from math import sin, cos

import sfml as sf

from Turret import TankTurret
from Player import PlayerTank, PlayerGun
from workarounds import check_sight


class EnemyTankTurret(TankTurret):
    def __init__(self, texture=sf.Texture.from_file("res/EnemyTankTurret.png")):
        TankTurret.__init__(self, texture)
        self.target = None

    def set_target(self, target):
        self.target = target

    def check_sight_to_target(self, objects):
        ret = True
        blockers = []
        for ob in objects:
            if ob.blocks_sight:
                blockers.append(ob)
        for blocker in blockers:
            if check_sight(self.position, self.target.position, blocker):
                ret = False
        return ret

    def check_angle_and_range(self):
        ret = False
        own_point = sf.Vertex()
        own_point.position = self.position
        far_point = sf.Vertex()
        far_point.position = (cos(self.rotation) * 100, sin(self.rotation) * 100)
        if check_sight(own_point.position, far_point.position, self.target):
            ret = True
        return ret

    def update(self, objects):
        if self.count >= self.reload_time:
            self.ready_to_fire = True
        else:
            self.count += 1
        self.position = self.tank.position
        for ob in objects:
            if isinstance(ob, PlayerTank) or isinstance(ob, PlayerGun):
                self.set_target(ob)
                self.change_facing(self.target.position)
                if self.check_sight_to_target(objects) and self.check_angle_and_range():
                    self.fire()

        for shell in self.shells:
            shell.update()
            if shell.dead:
                self.shells.remove(shell)
