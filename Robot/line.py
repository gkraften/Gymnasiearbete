from vector import Vector

class Line:
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction

    def distance_to(self, point):
        return ((self.start + (point - self.start).project_onto(self.direction)) - point).length()

    def __str__(self):
        return "(x, y) = {} + t{}".format(self.start, self.direction)