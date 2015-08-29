__author__ = 'John'

import sfml as sf


class LineOfSight(sf.VertexArray):
    def __init__(self, start_point, end_point):
        self.type = sf.PrimitiveType.LINES
        self.vertex_count = 2
        sf.VertexArray.__init__(self, self.type, self.vertex_count)
        self[0].position = start_point
        self[1].position = end_point
        for point in self:
            point.color = sf.Color.RED

    def check_sight(self, rect):
        ret = False
        # do y=mx+c for all values of x inside the left and right of the rectangle
        # calculate m as dy/dx
        dx = self[0].position.x - self[1].position.x
        dy = self[0].position.y - self[1].position.y
        m = dy / dx
        if dy == 0:
            m = 1
        elif dy == 0:
            m = 0

        # calculate c=y-mx
        c = self[0].position.y - m * self[0].position.x

        # for all points on the line, if y is between top and bottom and x is between left and right
        # return True
        for x in range(int(self[0].position.x), int(self[1].position.x)):
            y = m * x + c
            if rect.top < y < rect.bottom and rect.left < x < rect.right:
                # print "collision"
                self[1].color = sf.Color.YELLOW
                self[0].color = sf.Color.YELLOW
                ret = True
                break
        else:
            self[1].color = sf.Color.RED
            self[0].color = sf.Color.RED
        return ret

    def update(self, sight_blockers):
        for blocker in sight_blockers:
            self.check_sight(blocker.global_bounds)
