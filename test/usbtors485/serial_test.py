#!/usr/bin/env python

import serial
#import crc8
import time
import serial.rs485
import time


class Serial(object):

    def __init__(self):
        self.ser = serial.rs485.RS485(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

        self.ser.rs485_mode = serial.rs485.RS485Settings()
        self.count = 1

    def hexshow(self,argv):

        result = ''
        hLen = len(argv)

        for i in xrange(hLen):
            hvo1 = ord(argv[i])
            hhex = '%02x' % hvo1
            result = hhex

        print ('hexSHow:',result)
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
        packet.append(0x14)
        packet.append(0x01)
        packet.append(0x89)
        packet.append(0xAD)
        packet1 = bytearray()
        packet1.append(0xAC)
        packet1.append(0x20)
        packet1.append(0x42)
        packet1.append(0x01)
        packet1.append(0x06)
        packet1.append(0x10)
        packet1.append(0x80)
        packet1.append(0x00)
        packet1.append(0x1C)
        packet1.append(0x00)
        packet1.append(0x01)
        packet1.append(0x21)
        packet1.append(0x80)
        packet1.append(0x38)
        packet1.append(0xAD)
        packet2 = bytearray()
        packet2.append(0xAC)
        packet2.append(0x20)
        packet2.append(0x41)
        packet2.append(0x00)
        packet2.append(0x12)
        packet2.append(0x08)
        packet2.append(0x32)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x01)
        packet2.append(0x19)
        packet2.append(0xAA)
        packet2.append(0x5F)
        packet2.append(0x0C)
        packet2.append(0xC1)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x00)
        packet2.append(0x19)
        packet2.append(0x1A)
        packet2.append(0x36)
        packet2.append(0xAD)

        packet3 = "0xac"

        packet4 = "0xad"

        packet5 = bytearray()
        packet5.append(0xAC)
        packet5.append(0x00)
        packet5.append(0x01)
        packet5.append(0xB0)
        packet5.append(0x00)
        packet5.append(0xC9)
        packet5.append(0xAD)
        packet5.append(0xFF)



        packet6 = bytearray()
        packet6.append(0xAC)
        packet6.append(0x00)
        packet6.append(0x01)
        packet6.append(0x00)
        packet6.append(0x0D)
        packet6.append(0xBE)
        packet6.append(0xAD)
        packet6.append(0xFF)

        
        while True:
            #ser.write(b'\xAC\x30\x00\x2D\xAD')
            for line in self.ser.readline():
                print(hex(line))
            #     # if(hex(line) == packet3):
            #     #     time0 = time.time()

                if(hex(line) == packet4):
                    time.sleep(0.003)
                    if(self.count < 2):
                        self.ser.write(packet6)
                        self.count = self.count + 1
                    else: 
                        time.sleep(50)
            #             self.ser.write(packet5)
            #             print("send cmd")
            #         print(self.count)
                    # if ((time.time() - time0) > 0.02) :
                    #     print("one slop")




    #         #time.sleep(5)
            # self.ser.write(packet)
            # for line in self.ser.readline():
            #     print(hex(line))
            #     #if(hex(line) == "0xac"):
            #         #print("getgetget")
            # time.sleep(0.05)
            # self.ser.write(packet1)
            # time.sleep(0.05)
            # self.ser.write(packet2)
            # time.sleep(0.05)

    # # print("send")
    # # for line in ser.readline():
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