__author__ = 'John'

from math import atan2, degrees, sin, cos, radians

import sfml as sf

from workarounds import calc_shortest_direction

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
        angle = degrees(atan2(dy, dx)) + 90

        if angle < 0:
            # correct for (x, -y) quadrant
            angle += 360
            # if less than 3 degrees difference, snap to
        if abs(angle - self.rotation) < 3:
            self.rotation = angle
        else:
            if calc_shortest_direction(self.rotation, angle) >= 0:
                self.rotate(3)
            else:
                self.rotate(-3)

    def set_body(self, tank):
        self.tank = tank

    def get_forward_point(self):
        x = sin(radians(self.rotation)) * 10
        y = cos(radians(self.rotation)) * -10
        return self.position + sf.Vector2(x, y)

    def fire(self):
        if self.ready_to_fire:
            self.ready_to_fire = False
            self.count = 0
            s = Shell((sf.Texture.from_file("res/Shell.png")))
            s.setup(self, self.get_forward_point())
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
            self.fire()
        for shell in self.shells:
            shell.update()
            if shell.dead:
                self.shells.remove(shell)
