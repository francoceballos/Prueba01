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

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')

inputcmb="AT\r\n"
while 1 :
    
    # get keyboard input
    #inputcmb = raw_input(">> ")
    
    # Python 3 users
    inputcmb = input(">> ")
    
    if inputcmb == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write((inputcmb + "\r\n").encode('utf-8'))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)

        size = ser.inWaiting()
        print("\nDatos para leer en espera " + str(size))

        out = ser.read(size)

        #while ser.inWaiting() > 0:
        #    out += ser.read(1)

        if out != '':
            print (">>" + str(out) + "\n")