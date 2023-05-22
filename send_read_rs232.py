import time
import serial
import random
from app_ui.base_widget.utlis_func import *

# try:
#     ser = serial.Serial(
#         port='/dev/ttyUSB0',
#         baudrate=9600,
#         timeout=1,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS
#     )
# except Exception:
    # ShowNotification(AppStr.SCALE_ERROR_TITLE, AppStr.SCALE_ERROR, print('error'))
# while 1:
#     print(ser.readline())