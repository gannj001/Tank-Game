__author__ = 'John'

import math


def intersects(rect1, rect2):
    """
    Dumb Intersect function, if there is an intersection, returns true
    :param rect1: an sfml Rectangle (sf.Rectangle) object, no checking is done on the rectangle
    :param rect2: an sfml Rectangle (sf.Rectangle) object, no checking is done on the rectangle
    :return: boolean - if true, there is an intersection, else false
    """
    ret = False

    # compute the intersection boundaries
    left = max(rect1.left, rect2.left)
    top = max(rect1.top, rect2.top)
    right = min(rect1.right, rect2.right)
    bottom = min(rect1.bottom, rect2.bottom)

    # if the intersection is valid (positive non zero area), then
    # there is an intersection
    if left < right and top < bottom:
        ret = True
    return ret


def point_rect_intersect(point, rect):
    ret = False

    if rect.left <= point.x <= rect.right and rect.top <= point.y <= rect.bottom:
        ret = True

    return ret


def check_sight(point1, point2, sight_blocker):
    line = [point1, point2]
    rect = sight_blocker.global_bounds
    ret = True
    # do y=mx+c for all values of x inside the left and right of the rectangle
    # calculate m as dy/dx
    dx = line[0].position.x - line[1].position.x
    dy = line[0].position.y - line[1].position.y
    if dy == 0:
        m = 0
    elif dx == 0:
        m = 1
    else:
        m = dy / dx

    # calculate c=y-mx
    c = line[0].position.y - m * line[0].position.x

    # for all points on the line, if y is between top and bottom and x is between left and right
    # return True
    for x in range(int(line[0].position.x), int(line[1].position.x)):
        y = m * x + c
        if rect.top < y < rect.bottom and rect.left < x < rect.right:
            ret = False
    return ret


def get_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
