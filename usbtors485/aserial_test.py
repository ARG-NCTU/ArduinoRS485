#!/usr/bin/env python

import serial
import crc8
import time

ser = serial.Serial(port='/dev/ttyUSB1',baudrate = 19200,parity=serial.PARITY_NONE,\
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

def hexshow(argv):

    result = ''
    hLen = len(argv)

    for i in xrange(hLen):
        hvo1 = ord(argv[i])
        hhex = '%02x' % hvo1
        result = hhex

    print 'hexSHow:',result
    return result

print("connected to :"+ser.portstr)

pkg = "0x300x820x080x640xAA"
#pkg = "0xAC0x300x01"

packet = bytearray()
packet.append(0xAC)
packet.append(0x30)
packet.append(0x82)
packet.append(0x08)
packet.append(0x64)
packet.append(0xAA)
packet.append(0xCF)
packet.append(0xAD)



#print(hex(8))
#print(hex(300))
#ser.open()
while True:
    #ser.write(b'\xAC\x30\x00\x2D\xAD')
    #time.sleep(5)
    #ser.write(packet)
    #print("send")
    for line in ser.readline():
        print(hexshow(line))
        print(type(hexshow(line)))
    #in_hex = ser.read()
    ##print(type(in_hex))


#ser.write("0xAC0x300x000x2C0xAD")

#ser.write("0xAC0x300x000x2C0xAD")
    #print('send')
#line=ser.readlines()
#print(line)

ser.close()