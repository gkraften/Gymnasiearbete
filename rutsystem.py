import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def in_rect(point, pos, size):
    return point[0] > pos[0] and point[0] < pos[0] + size and point[1] > pos[1] and point[1] < pos[1] + size

file = input("Välj fil: ")

points = []
points_x = []
points_y = []
with open(file) as f:
    for line in f:
        parts = line.split(",")
        points.append([float(parts[0]), float(parts[1])])
        points_x.append(float(parts[0]))
        points_y.append(float(parts[0]))

size = float(input("Välj storlek på rutnät: ").replace(",", "."))
threshold = int(input("Välj tröskelvärde: "))
title = input("Titel: ")

rectangles = []
to_remove = []
while len(points) > 0:
    start = points[0]
    rect = (size * (start[0]//size), size * (start[1]//size))
    p_in_rect = 1
    to_remove.append(0)

    for i in range(1, len(points)):
        p = points[i]
        if in_rect(p, rect, size):
            p_in_rect += 1
            to_remove.append(i)

    points = [v for i, v in enumerate(points) if i not in to_remove]
    to_remove = []

    if p_in_rect >= threshold:
        rectangles.append(rect)


plt.title(title)

plt.xlabel("cm")
plt.ylabel("cm")

plt.xlim((min(points_x), max(points_x)))
plt.ylim((min(points_y), max(points_y)))

print(len(rectangles))
for rect in rectangles:
    plt.gca().add_patch(Rectangle(rect, size, size))

plt.show()