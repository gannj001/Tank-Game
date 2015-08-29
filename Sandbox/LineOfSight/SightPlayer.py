__author__ = 'John'

import sfml as sf

from Sandbox.LineOfSight import LineOfSight


class SightPlayer(sf.CircleShape):
    def __init__(self, x, y):
        sf.CircleShape.__init__(self)
        self.radius = 10
        self.position = (x, y)
        self.outline_color = sf.Color.BLUE
        self.outline_thickness = 5
        self.los = None

    def update(self, sight_blockers, mouse_position):
        self.los = LineOfSight(self.position, mouse_position)
        self.los.update(sight_blockers)
