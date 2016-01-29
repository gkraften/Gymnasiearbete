import queue
import threading
import socket
import json
import time

_mapfile = None
_data = queue.Queue()
_s = None
_connection = False
_running = False
_conn = None
_addr = None

def _handle_connection():
    global _s
    global _connection
    global _conn
    global _addr

    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.bind(("", 1234))
    _s.listen(1)
    try:
        _conn, _addr = _s.accept()
    except:
        return
    print("Anslutning från {}:1234".format(_addr[0]))
    _connection = True

def _handle_data():
    global _running
    global _data
    global _connection
    global _mapfile
    global _conn
    global _addr

    last = time.time()
    while _running:
        position = []
        walls = []
        heading = None

        while not _data.empty():
            d = _data.get(timeout=0.5)
            if "walls" in d:
                walls += d["walls"]
            if "position" in d:
                position += d["position"]
            if "heading" in d:
                heading = d["heading"]

        data = {}
        if len(walls) > 0:
            data["walls"] = walls
        if len(position) > 0:
            data["position"] = position
        if not heading is None:
            data["heading"] = heading

        if len(data) > 0:
            if not _mapfile is None and not _mapfile.closed:
                for wall in walls:
                    print("{},{}".format(wall[0], wall[1]), file=_mapfile)

            if _connection:
                try:
                    _conn.sendall(json.dumps(data).encode("utf-8"))
                except:
                    _conn.close()
                    _s.close()
                    _connection = False
                    print("Förlorade anslutning till {}".format(_addr[0]))

        if time.time() - last < 5:
            time.sleep(5 - (time.time() - last))
        last = time.time()
    _running = False

def initialize(file):
    global _mapfile
    global _running

    _running = True
    _mapfile = open(file, "w")
    t = threading.Thread(target=_handle_connection)
    t.setDaemon(True)
    t.start()
    threading.Thread(target=_handle_data).start()

def close():
    global _connection
    global _conn
    global _mapfile
    global _data
    global _running

    while _running:
        pass
    if _connection:
        _conn.close()
    _s.close()
    _mapfile.close()
    _connection = False
    _running = False

def log(**data):
    _data.put(data)