__author__ = 'John'

import sfml as sf

from workarounds import check_sight, get_distance, point_rect_intersect


class Path(sf.VertexArray):
    def __init__(self, start_point, end_point):
        self.type = sf.PrimitiveType.LINES
        self.vertex_count = 2
        sf.VertexArray.__init__(self, self.type, self.vertex_count)
        self[0].position = start_point
        self[1].position = end_point
        for point in self:
            point.color = sf.Color.RED

    def update(self, sight_blockers):
        # split out pathfinding and sighting functions
        # if player can be seen, and is in range, stop and fire
        # else move towards player along path
        for blocker in sight_blockers:
            while not check_sight(self[0], self[1], blocker):
                # set old dist as current dist
                olddist = get_distance(self[0].position, self[1].position)
                tx = int(self[1].position.x)
                ty = int(self[1].position.y)

                # setup points to check
                for x in [tx - 5, tx, tx + 5]:
                    for y in [ty - 5, ty, ty + 5]:
                        if not point_rect_intersect(sf.Vector2(x, y), blocker.global_bounds):
                            newdist = get_distance(self[0].position, sf.Vector2(x, y))
                            if newdist < olddist:
                                olddist = newdist
                                newpos = x, y

                # add newpos to vertex array
                v = sf.Vertex()
                v.position = sf.Vector2(newpos[0], newpos[1])
                v.color = sf.Color.RED

                self.append(self[1])
                self[1] = v

                for i in range(len(self)):
                    print "Point #" + str(i) + ": " + str(self[i].position.x), str(self[i].position.y)
