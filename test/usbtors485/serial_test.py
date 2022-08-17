#!/usr/bin/env python

import serial
#import crc8
import time
import serial.rs485
import time
from crccheck.crc import Crc8Maxim


class Serial(object):

    def __init__(self):
        self.ser = serial.rs485.RS485(port='/dev/ttyUSB0',baudrate = 19200,parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
        #self.ser.open()
        self.ser.rs485_mode = serial.rs485.RS485Settings()
        self.count = 0
        self.once = 0

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

    def tohex(self,val, nbits):
        hex_cmd = hex((val + (1 << nbits)) % (1 << nbits))
        hex_string = ""
        length = len(hex_cmd)
        zero = 6-length
        for i in range(zero):
            hex_string = hex_string + "0"
        data = hex_cmd[2:length]
        hex_string = hex_string+data
        data1 = bytearray.fromhex(hex_string)
        return data1

    def vel_to_hex_cmd(self,vel):
        self.packet = bytearray()
        self.packet.append(0xAC)
        self.packet.append(0x00)
        self.packet.append(0x00)
        self.packet.append(0x05)
        self.packet.append(0x00)
        hex_cmd = self.tohex(vel,16)
        self.packet.extend(hex_cmd)
        crc = Crc8Maxim.calc(self.packet[1:])
        self.packet.extend(crc.to_bytes(1,'big'))
        self.packet.append(0xAD)
        print(self.packet)
        return self.packet

#ser.open()
# 
    def send(self):

        cmd_vel = self.vel_to_hex_cmd(300)
        cmd_vel2 = self.vel_to_hex_cmd(-300)



        packet3 = "0xad"

        packet4 = "0x89"

        packet5 = bytearray()
        packet5.append(0xAC)
        packet5.append(0x00)
        packet5.append(0x00)
        packet5.append(0x05)
        packet5.append(0x00)
        packet5.append(0x02)
        packet5.append(0x2D)
        packet5.append(0xCE)
        packet5.append(0xAD)
        packet5.append(0xFF)



        packet6 = bytearray()
        packet6.append(0xAC)
        packet6.append(0x00)
        packet6.append(0x00)
        packet6.append(0x05)
        packet6.append(0x00)
        packet6.append(0x00)
        packet6.append(0x00)
        packet6.append(0x81)
        packet6.append(0xAD)
        packet6.append(0xFF)

   
        while True:
           
            #ser.write(b'\xAC\x30\x00\x2D\xAD')
            for line in self.ser.readline():
                print(hex(line))
            #     # if(hex(line) == packet3):
            #     #     time0 = time.time()
                
                if(hex(line) == packet4):
                    self.count = 1

                if(hex(line) == packet3):
                    if (self.count == 1):
                        #time.sleep(0.003)
                        #print(self.once)
                        if (self.once < 5):
                            print("send reset")
                            self.ser.write(packet6)
                            self.count = 0
                            self.once = self.once+1
                        elif(self.once<10):
                            print("send speed")
                            self.ser.write(cmd_vel)
                            self.once = self.once+1
                            self.count = 0
                        elif(self.once<15):
                            print("send reset")
                            self.ser.write(packet6)
                            self.count = 0
                            self.once = self.once+1
                        elif(self.once<45):
                            print("send negative speed")
                            self.ser.write(cmd_vel2)
                            self.once = self.once+1
                            self.count = 0
                        elif(self.once<75):
                            print("send speed")
                            self.ser.write(cmd_vel)
                            self.once = self.once+1
                            self.count = 0


        print("close")
        self.ser.close()




            #             self.ser.write(packet5)
            #             print("send cmd")
            #         print(self.count)
                    # if ((time.time() - time0) > 0.02) :
                    #     print("one slop")





if __name__ == "__main__":
    sendpacket = Serial()
    sendpacket.send()