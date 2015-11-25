from vector import Vector
from line import Line
import math

l = Line(Vector(0, 0), Vector(1, 1))
p = Vector(1, 3)

print(p)
print(l)
print(p.distance_to(l))