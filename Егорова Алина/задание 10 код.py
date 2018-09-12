#10.Заданы координаты прямоугольников на плоскости (не более 10). Определить координаты минимального по размерам прямоугольника, охватывающего заданные. Обеспечить поиск прямоугольников, охватывающих точку с заданными координатами.



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, LB, LT, RT, RB):
        self.LB = LB
        self.LT = LT
        self.RT = RT
        self.RB = RB

    def contain(self, point):
        x = point.x
        y = point.y

        LB = self.LB
        LT = self.LT
        RT = self.RT

        if y <= LT.y and y >= LB.y and x >= LT.x and x <= RT.x:
            return True
        else:
            return False


LB1 = Point(1, 1)
LT1 = Point(1, 4)
RT1 = Point(4, 4)
RB1 = Point(4, 1)
rec1 = Rectangle(LB1, LT1, RT1, RB1)

LB2 = Point(6, 6)
LT2 = Point(6, 9)
RT2 = Point(9, 9)
RB2 = Point(6, 9)
rec2 = Rectangle(LB2, LT2, RT2, RB2)


def find_outermost_points(rectangles):
    firstRectangle = rectangles[0]
    outermostBottom = firstRectangle.LB.y
    outermostLeft = firstRectangle.LB.x
    outermostTop = firstRectangle.RT.y
    outermostRight = firstRectangle.RT.x

    for rectangle in rectangles:
        bottom = rectangle.LB.y
        left = rectangle.LB.x
        top = rectangle.RT.y
        right = rectangle.RT.x

        if outermostBottom > bottom:
            outermostBottom = bottom
        if outermostLeft > left:
            outermostLeft = left
        if outermostTop < top:
            outermostTop = top
        if outermostRight < right:
            outermostRight = right

    # return [outermostBottom, outermostLeft, outermostTop, outermostRight]
    return {
        'outermostBottom': outermostBottom,
        'outermostLeft': outermostLeft,
        'outermostTop': outermostTop,
        'outermostRight': outermostRight
    }


def build_rectangle_by_points(points):
    outermostBottom = points['outermostBottom']
    outermostLeft = points['outermostLeft']
    outermostTop = points['outermostTop']
    outermostRight = points['outermostRight']

    LB = Point(outermostLeft, outermostBottom)
    LT = Point(outermostLeft, outermostTop)
    RT = Point(outermostRight, outermostTop)
    RB = Point(outermostRight, outermostBottom)

    return Rectangle(LB, LT, RT, RB)


# First Task
def find_the_rectangle(rectangles):
    points = find_outermost_points(rectangles)
    return build_rectangle_by_points(points)


# Second Task
def find_rectangles_containing_the_point(rectangles, point):
    res = []
    for rectangle in rectangles:
        if rectangle.contain(point):
            res.append(rectangle)

    return res
