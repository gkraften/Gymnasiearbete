import smbus
import math

DEVICE_ADDRESS = 0x1e
REGISTER_CRA_REG_M = 0x00
REGISTER_CRB_REG_M = 0x01
REGISTER_MR_REG_M = 0x02
REGISTER_OUT_X_H_M = 0x03
REGISTER_OUT_X_L_M = 0x04
REGISTER_OUT_Z_H_M = 0x05
REGISTER_OUT_Z_L_M = 0x06
REGISTER_OUT_Y_L_M = 0X08
REGISTER_OUT_Y_H_M = 0X07

_xoffset = -253.0
_yoffset = -176.5
_xscale = 0.003952569169960474
_yscale = 0.0056657223796034

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

    x = (_twos_comp(((xh & 0xff)<<8) | xl, 16) + _xoffset) * _xscale
    y = (_twos_comp(((yh & 0xff)<<8) | yl, 16) + _yoffset) * _yscale
    z = _twos_comp(((zh & 0xff)<<8) | zl, 16)

    return (x, y, z)

def getHeading():
    values = readAxisData()
    return math.degrees(math.atan2(values[1], values[0]))

setNormalSpeedDataRate()
bus.write_byte_data(DEVICE_ADDRESS, REGISTER_CRB_REG_M, 0x20)
