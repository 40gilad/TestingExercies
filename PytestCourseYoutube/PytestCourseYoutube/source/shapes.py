import math


class Shape:
    _area = -1
    _perimeter = -1

    def area(self):
        return self._area

    def perimeter(self):
        return self._perimeter

    def __eq__(self, other):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self._area = math.pi * (self.radius ** 2)
        self._perimeter = 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = width * length
        self._perimeter = (width * 2) + (length * 2)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return other.width == self.width and other.length == self.length


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self._area = length ** 2
        self._perimeter = length * 4
