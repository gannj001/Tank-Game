__author__ = 'John'

import math

import sfml as sf

from workarounds import intersects


class TankBody(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(texture)
        self.origin = (16, 24)
        self.accel = 0.1
        self.turret = None
        self.traverse = 1
        self.top_speed = 2
        self.speed = 0
        self.blocks_sight = False
        self.blocks_movement = True

    def check_collisions(self, objects):
        move_blockers = []
        for ob in objects:
            if ob == self:
                continue
            else:
                if ob.blocks_movement:
                    move_blockers.append(ob)

        for blocker in move_blockers:
            own_rect = self.global_bounds
            ob_rect = blocker.global_bounds
            if intersects(own_rect, ob_rect):
                dx = own_rect.center.x - ob_rect.center.x
                dy = own_rect.center.y - ob_rect.center.y
                angle = math.atan2(dy, dx) + 90
                if angle < 0:
                    angle += 360

                if 45 < angle <= 135:
                    self.position.x = blocker.global_bounds.right
                elif 135 < angle <= 225:
                    self.position.y = blocker.global_bounds.bottom
                elif 225 < angle <= 315:
                    self.position.x = blocker.global_bounds.left + self.local_bounds.width / 2
                else:
                    self.position.y = blocker.global_bounds.top + self.local_bounds.height / 2

    def set_turret(self, turret):
        self.turret = turret

    def rotate_left(self):
        self.rotate(-self.traverse)
        self.turret.rotate(-self.traverse)

    def rotate_right(self):
        self.rotate(self.traverse)
        self.turret.rotate(self.traverse)

    def forward(self):
        self.speed += self.accel
        if self.speed > self.top_speed:
            self.speed = self.top_speed

    def backward(self):
        self.speed -= self.accel
        if self.speed < -self.top_speed:
            self.speed = -self.top_speed

    def slow_down(self):
        if self.speed > 0:
            self.speed -= self.accel
        elif self.speed < 0:
            self.speed += self.accel
        self.speed = round(self.speed, 1)

    def calc_position(self):
        x = math.sin(math.radians(self.rotation)) * self.speed
        y = math.cos(math.radians(self.rotation)) * -self.speed
        self.position += (x, y)

    def move(self, keyboard):
        if keyboard.is_key_pressed(sf.Keyboard.A):
            self.rotate_left()
        elif keyboard.is_key_pressed(sf.Keyboard.D):
            self.rotate_right()

        if keyboard.is_key_pressed(sf.Keyboard.W):
            self.forward()
        elif keyboard.is_key_pressed(sf.Keyboard.S):
            self.backward()
        else:
            self.slow_down()
        self.calc_position()

    def check_edge(self, window):
        if self.position.x < 0:
            self.position = (0, self.position.y)
        elif self.position.x > window.size.x:
            self.position = (window.size.x, self.position.y)

        if self.position.y < 0:
            self.position = (self.position.x, 0)
        elif self.position.y > window.size.y:
            self.position = (self.position.x, window.size.y)

    def update(self, mouse, window, keyboard, objects):
        if sf.KeyEvent.pressed:
            self.move(keyboard)
        else:
            self.slow_down()

        self.check_collisions(objects)

        self.check_edge(window)
        self.turret.update(mouse, window)
