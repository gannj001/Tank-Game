__author__ = 'John'

import sfml as sf

from Path import Path


class PathfinderPlayer(sf.CircleShape):
    def __init__(self, x, y):
        sf.CircleShape.__init__(self)
        self.radius = 10
        self.position = (x, y)
        self.outline_color = sf.Color.BLUE
        self.outline_thickness = 5
        self.path = None

    def update(self, sight_blockers, mouse_position):
        self.path = Path(self.position, mouse_position)
        self.path.update(sight_blockers)
