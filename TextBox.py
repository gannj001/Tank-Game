__author__ = 'John'

from Button import Button


class TextBox(Button):
    def __init__(self, texture):
        Button.__init__(self, texture)

    def update(self, mouse_position):
        pass
