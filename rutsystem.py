import matplotlib.pyplot as plt

file = input("Välj fil: ")
size = float(input("Välj storlek på rutnät: "))
threshold = int(input("Välj tröskelvärde: "))
title = input("Titel: ")

points = []
with open(file) as f:
    for line in f:
        parts = line.split(",")
        points.append([float(parts[0]), float(parts[1])])
print(len(points))

plt.title(title)

plt.xlabel("cm")
plt.ylabel("cm")

plt.plot([1, 2], [1, 2])

plt.show()