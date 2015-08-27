__author__ = 'John'


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
