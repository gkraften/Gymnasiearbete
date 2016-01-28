import urllib.request
import matplotlib.pyplot as plt

urllib.request.urlretrieve("http://lillefar.local/map.txt", "map.txt")

x = []
y = []
with open("map.txt") as f:
    for line in f:
        coords = line.split(",")
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.scatter(x, y)
plt.scatter([0], [0], c="pink")
plt.show()