__author__ = 'John'

import sfml as sf

from Tank import TankBody
from Shell import Shell
from Player import PlayerTank, PlayerGun
from EnemyTurret import EnemyTankTurret
from workarounds import *
from Path import Path


class EnemyTank(TankBody):
    def __init__(self, texture=sf.Texture.from_file("res/EnemyTankBody.png")):
        TankBody.__init__(self, texture)
        turret = EnemyTankTurret()
        turret.set_body(self)
        self.target = None
        self.path = None

    def check_shells(self, objects):
        for ob in objects:
            if isinstance(ob, Shell):
                if intersects(ob.global_bounds, self.global_bounds):
                    self.health -= ob.damage
                    objects.remove(ob)

    def check_sight_to_target(self, objects):
        blockers = []
        for ob in objects:
            if ob.blocks_sight:
                blockers.append(ob)
        return check_sight(self.position, self.target.position, blockers)

    def move(self):
        dx = self.path[1].position.x - self.position.x
        dy = self.path[1].position.y - self.position.y
        angle = math.degrees(math.atan2(dy, dx)) + 90
        if abs(angle - self.rotation) < 3:
            self.rotation = angle
        else:
            if angle > self.rotation:
                self.rotate(3)
            elif angle < self.rotation:
                self.rotate(-3)

        if abs(angle - self.rotation) < 10:
            self.forward()
            # elif 170 < abs(angle - self.rotation) < 190:
            #     self.backward()

    def update(self, objects):
        for ob in objects:
            if isinstance(ob, PlayerTank) or isinstance(ob, PlayerGun):
                self.target = ob

        if self.target:
            sight = self.check_sight_to_target(objects)
            if not sight:
                self.path = Path(self.position, self.target.position)
                self.move()
            else:
                self.slow_down()

        self.check_shells(objects)
