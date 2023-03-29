import time
import serial
import random
def readRs232():
    ser = serial.Serial(
        port='COM6',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()
    # Reading the data from the serial port.
    for i in range(20):
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        time.sleep(1)
        print(data)
        dataStr = str(data).replace("b\'", "").replace("\'","")
        if dataStr != "":
            return dataStr
# readRs232()
# def sendRs232():
#     serPort = serial.Serial(port= 'COM10')
#     while True:
#         data = random.randint(1, 200)
#         print(data)
#         serPort.write(str(data))
#         print('sent')
#         time.sleep(1)
# sendRs232()

def sendRs232():
    ser = serial.Serial(
        port='COM5',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()
    # Reading the data from the serial port.
    while True:
        ser.write('1'.encode())
        print('1'.encode())
        time.sleep(1)
# sendRs232()