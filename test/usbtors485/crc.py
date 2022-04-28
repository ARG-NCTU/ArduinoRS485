#!/usr/bin/env python

uint8_t crc8_calculate(uint8_t data, uint8_t crc){
 2 
 3     int i = 0;
 4     uint8_t crc_poly = 0x07;
 5     crc ^= data;
 6 
 7     for(i = 0; i < 8; i++){
 8 
 9         if(crc & 0x80){
10             crc <<= 1;
11             crc ^= crc_poly;
12         }
13         else
14             crc <<= 1;
15     }
16     return (crc & 0xFF);
17 }