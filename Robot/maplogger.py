import queue
import threading
import socket

_mapfile = None
_data = queue.Queue()
_s = None
_connection = False
_running = True

def set_map_file(f):
    global _mapfile
    if not _mapfile is None:
        _mapfile.close()
    _mapfile = open(f, "w")

def _handle_connection():
    global _s
    global _connection

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 1234))
    s.listen(1)
    try:
        conn, addr = s.accept()
    except:
        return
    print("Anslutning från {}:1234".format(addr[0]))
    _connection = True

def _handle_data():
    global _running
    global _data
    global _connection
    global _mapfile

    while _running:
        data = None
        try:
            data = _data.get(timeout=1)
        except queue.Empty:
            continue

        #Förbättra, skicka inte en sak i taget och spara bara väggar till fil (helst färdväg med)