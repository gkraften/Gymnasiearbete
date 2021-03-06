import sys
import socket
from threading import Thread
import json
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

try:
    s.connect(("lillefar.local", 1234))
except:
    try:
        host = input("Skriv Lillefars IP: ")

        if len(host) == 0:
            sys.exit()
        print("Ansluter till {}:{}".format(host, 1234))
        s.connect((host, 1234))
    except:
        print("Kunde inte ansluta till Lillefar")
        sys.exit()
print("Ansluten!")
s.settimeout(0)


import matplotlib.pyplot as plt

x = []
y = []
pos_x = [0]
pos_y = [0]
heading = 0

def update_plot():
    global s
    global x
    global y
    global pos_x
    global pos_y
    global heading
    while True:
        success = False
        res = ""
        disconnection = False
        while not success:
            try:
                while not res.endswith("}"):
                    r = s.recv(1024).decode("utf-8")
                    if len(r) == 0:
                        disconnection = True
                        break
                    res += r
                success = True
            except:
                pass
        if disconnection:
            print("Anslutning förlorad")
            break

        try:
            data = []
            parts = [e+"}" for e in res.split("}") if e != ""]
            for part in parts:
                data.append(json.loads(part))
        except json.decoder.JSONDecodeError:
            print(res)

        for d in data:
            if "walls" in d:
                for wall in d["walls"]:
                    x.append(wall[0])
                    y.append(wall[1])
            if "position" in d:
                for position in d["position"]:
                    pos_x.append(position[0])
                    pos_y.append(position[1])
            if "heading" in d:
                heading = d["heading"]

        try:
            plt.cla()
            plt.scatter(x, y)
            plt.plot(pos_x, pos_y, c="pink")
            length = abs(plt.xlim()[0] - plt.xlim()[1])/20
            plt.arrow(pos_x[-1], pos_y[-1], length/10*math.cos(heading), length/10*math.sin(heading), fc="pink", ec="pink", head_length=length, head_width=length/2)
            plt.xlabel("~Norr")
            plt.ylabel("~Väst")
            plt.draw()
        except:
            print(data)


plt.scatter([0], [0], c="pink")

plt.xlabel("~Norr")
plt.ylabel("~Väst")

t = Thread(target=update_plot)
t.setDaemon(True)
t.start()

plt.show()
s.close()