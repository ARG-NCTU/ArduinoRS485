#!/usr/bin/env python

import serial
import crc8
import time
import serial.rs485

class Serial_receive(object):

    def __init__(self):
        self.ser = serial.rs485.RS485(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

        self.ser.rs485_mode = serial.rs485.RS485Settings()

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
    def receive(self):
        while True:
            #print("packet start")
            for line in self.ser.readline():
                print(hex(line))
                #print("packet end")
                #print(type(self.hexshow(line)))

            #print("packet end")


#ser.write("0xAC0x300x000x2C0xAD")

#ser.write("0xAC0x300x000x2C0xAD")
    #print('send')
#line=ser.readlines()
#print(line)

#ser.close()

if __name__ == "__main__":
    sendpacket = Serial_receive()
    sendpacket.receive()