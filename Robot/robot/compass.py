import smbus
import math
import time

DEVICE_ADDRESS = 0x1e
REGISTER_CRA_REG_M = 0x00
REGISTER_CRB_REG_M = 0x01
REGISTER_MR_REG_M = 0x02
REGISTER_OUT_X_H_M = 0x03
REGISTER_OUT_X_L_M = 0x04
REGISTER_OUT_Z_H_M = 0x05
REGISTER_OUT_Z_L_M = 0x06
REGISTER_OUT_Y_L_M = 0x08
REGISTER_OUT_Y_H_M = 0x07

_xoffset = 197.5 - 72 + 32.5 - 23
_yoffset = -113 - 74 + 10 + 5

bus = smbus.SMBus(1)

def _twos_comp(val, bits):
    if (val & (1<<(bits-1))) != 0:
        return val - (1<<bits)
    return val

def wake():
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER_MR_REG_M, 0)

def sleep():
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER_MR_REG_M, 2)

def setHighSpeedDataRate():
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER_CRA_REG_M, 0x1c) # 220Hz

def setNormalSpeedDataRate():
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER_CRA_REG_M, 0x10) # 15Hz

def readAxisData():
    xl = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_X_L_M)
    xh = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_X_H_M)
    yl = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_Y_L_M)
    yh = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_Y_H_M)
    zl = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_Z_L_M)
    zh = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_OUT_Z_H_M)

    x = _twos_comp(((xh & 0xff)<<8) | xl, 16) - _xoffset
    y = _twos_comp(((yh & 0xff)<<8) | yl, 16) - _yoffset
    z = _twos_comp(((zh & 0xff)<<8) | zl, 16)

    return (x, y, z)

def getHeading():
    values = readAxisData()
    angle = math.atan2(values[1], values[0])
    if angle < 0:
        angle += 2*math.pi
    return 2*math.pi - angle

def angleDifference(v, w):
    '''Ger skillnaden mellan v och w. Är talet positivt betyder det att v ligger längre motsols än w; är talet negativt ligger v längre medsols än w.'''
    return math.atan2(math.sin(v-w), math.cos(v-w))

def calibrate(duration):
    global _xoffset
    global _yoffset

    x = []
    y = []
    t = time.time()
    while time.time() - t < duration:
        p = readAxisData()
        x.append(p[0])
        y.append(p[1])
        time.sleep(1/220)

    distances = []
    for i in range(1, len(x)):
        p1 = (x[i-1], y[i-1])
        p2 = (x[i], y[i])
        distances.append(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

    average_distance = sum(distances)/len(distances)
    for i in range(1, len(x)):
        p1 = (x[i-1], y[i-1])
        p2 = (x[i], y[i])
        if math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) > average_distance + 20:
            x.remove(x[i])
            y.remove(y[i])

    _xoffset += (min(x) + max(x))/2
    _yoffset += (min(y) + max(y))/2

setHighSpeedDataRate()
bus.write_byte_data(DEVICE_ADDRESS, REGISTER_CRB_REG_M, 0x20)
