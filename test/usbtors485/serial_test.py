#!/usr/bin/env python

import serial
import crc8
import time


class Serial(object):

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

        print("connected to :"+self.ser.portstr)

    def hexshow(self,argv):

        result = ''
        hLen = len(argv)

        for i in xrange(hLen):
            hvo1 = ord(argv[i])
            hhex = '%02x' % hvo1
            result = hhex

        print 'hexSHow:',result
        return result


# pkg = "0x300x820x080x640xAA"
# #pkg = "0xAC0x300x01"


#print(hex(8))
#print(hex(300))
#ser.open()
# 
    def send(self):
        packet = bytearray()
        packet.append(0xAC)
        packet.append(0x30)
        packet.append(0x82)
        packet.append(0x01)
        packet.append(0x64)
        packet.append(0xAA)
        packet.append(0x41)
        packet.append(0xAD)
        while True:
            #ser.write(b'\xAC\x30\x00\x2D\xAD')
            #time.sleep(5)
            self.ser.write(packet)
            time.sleep(1)

    # print("send")
    # for line in ser.readline():
    #    print(hexshow(line))
    #    print(type(hexshow(line)))
    # in_hex = ser.read()
    # print(type(in_hex))
    # time.sleep(0.5)


#ser.write("0xAC0x300x000x2C0xAD")

#ser.write("0xAC0x300x000x2C0xAD")
    #print('send')
#line=ser.readlines()
#print(line)

#ser.close()

if __name__ == "__main__":
    sendpacket = Serial()
    sendpacket.send()