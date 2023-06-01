import time
import serial
from app_ui.base_widget.utlis_func import *
try: 
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
except Exception:
    ShowNotification(AppStr.SCALE_ERROR_TITLE, AppStr.SCALE_ERROR, print('error'))

ser.isOpen()
# Reading the data from the serial port. This will be running in an infinite loop.
# for i in range(10):
#     bytesToRead = ser.inWaiting()
#     data = ser.read(bytesToRead)
#     time.sleep(2)
#     print(data)
#     dataStr = str(data).replace("b\'", "").replace("\'","")
#     print(dataStr)

# while 1 :
#     print(ser.readline())
