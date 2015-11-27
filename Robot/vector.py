import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def lengthsq(self):
        return self.x**2 + self.y**2

    def angle(self):
        return math.atan2(self.x, self.y)

    def to_polar(self):
        return (self.length(), self.angle())

    def project_onto(self, other):
        return ((self*other)/other.lengthsq())*other

    def normalized(self):
        return self/self.length()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rmul__(self, other):
        return Vector(other*self.x, other*self.y)

    def __neg__(self):
        return -1*self

    def __mul__(self, other):
        if type(other) != type(self):
            raise ValueError("Scalar produkt must be between two vectors!")

        return self.x*other.x + self.y*other.y

    def __truediv__(self, other):
        return Vector(self.x/other, self.y/other)


def from_polar(radius, angle):
    return Vector(radius*math.cos(angle), radius*math.sin(angle))