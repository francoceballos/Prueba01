#! /usr/bin/python3.7

#Link libreria manejo puerto serie python3
#https://pyserial.readthedocs.io/en/latest/pyserial_api.html?highlight=encode
#https://julioecheverri.wordpress.com/2018/02/26/comunicacion-serial-y-python/

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    write_timeout=2,
    timeout=5
)

ser.isOpen()


ser.write(("\r\n").encode('utf-8'))

while 1 :
    
    # get keyboard input
    #inputcmb = raw_input(">> ")
    
    # Python 3 users
    
    
        
    # send the character to the device
    # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
    out = ''
    size = ser.inWaiting()

    out = ser.read(size)

    if out != '':
        print (">>" + str(out) + "\n")