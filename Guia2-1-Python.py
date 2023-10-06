import serial
import time

class SerialCom:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def read(self):
        if self.ser.in_waiting > 0:
            return self.ser.readline().decode('utf-8').rstrip()

    def write(self, data):
        self.ser.write(data.encode())

com = SerialCom('/dev/ttyUSB0', 9600)
while True:
    data = com.read()
    if data:
        print(data)
        com.write(data)
