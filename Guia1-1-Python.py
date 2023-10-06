import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    read_ser=ser.readline()
    print(read_ser)
    if(read_ser=="Hola Raspberry"):
        blink(11)
