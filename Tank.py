__author__ = 'John'

import math

import sfml as sf


class TankBody(sf.Sprite):
    def __init__(self, texture):
        sf.Sprite.__init__(texture)
        self.origin = (16, 24)
        self.speed = 3
        self.turret = None

    def set_turret(self, turret):
        self.turret = turret

    def rotate_left(self):
        self.rotate(-3)

    def rotate_right(self):
        self.rotate(3)

    def forward(self):
        x = math.sin(math.radians(self.rotation)) * self.speed
        y = math.cos(math.radians(self.rotation)) * -self.speed
        self.position += (x, y)

    def backward(self):
        x = math.sin(self.rotation) * -self.speed
        y = math.cos(self.rotation) * self.speed
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

    def update(self, mouse, window, keyboard):
        self.turret.update(mouse, window)
        if sf.KeyEvent.pressed:
            self.move(keyboard)
