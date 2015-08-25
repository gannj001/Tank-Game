__author__ = 'John'

import math

import sfml as sf

from Shell import Shell


class TankTurret(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(texture)
        self.origin = (6, 30)
        self.reload_time = 20
        self.ready_to_fire = True
        self.count = 0
        self.shells = []
        self.tank = None
        self.shells_fired = 0

    def change_facing(self, mouse_position):
        dx = mouse_position.x - self.position.x
        dy = mouse_position.y - self.position.y
        angle = math.degrees(math.atan2(dy, dx)) + 90
        self.rotation = angle

    def set_body(self, tank):
        self.tank = tank

    def fire(self, mouse_position):
        if self.ready_to_fire:
            self.ready_to_fire = False
            self.count = 0
            s = Shell((sf.Texture.from_file("res/Shell.png")))
            s.setup(self, mouse_position)
            self.shells.append(s)
            self.shells_fired += 1

    def update(self, mouse, window):
        if self.count >= self.reload_time:
            self.ready_to_fire = True
        else:
            self.count += 1
        self.position = self.tank.position
        self.change_facing(mouse.get_position(window))
        if mouse.is_button_pressed(sf.Mouse.LEFT):
            self.fire(mouse.get_position(window))
        for shell in self.shells:
            shell.update()
            if shell.dead:
                self.shells.remove(shell)
