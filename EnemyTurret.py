__author__ = 'John'

import sfml as sf

from Turret import TankTurret
from Player import PlayerTank, PlayerGun
from workarounds import check_sight


class EnemyTankTurret(TankTurret):
    def __init__(self, texture=sf.Texture.from_file("res/EnemyTankTurret.png")):
        TankTurret.__init__(texture)
        self.target = None

    def set_target(self, target):
        self.target = target

    def check_sight_to_target(self, objects):
        blockers = []
        for ob in objects:
            if ob.blocks_sight:
                blockers.append(ob)
        return check_sight(self.position, self.target.position, blockers)

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
                if self.check_sight_to_target(objects):
                    self.fire(self.target.position)

        for shell in self.shells:
            shell.update()
            if shell.dead:
                self.shells.remove(shell)
