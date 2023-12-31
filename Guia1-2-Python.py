import smbus2 as smbus
import time

bus = smbus.SMBus(1) # Indica que estamos usando el bus I2C número 1
time.sleep(0.5)

address = 0x08

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    var = input("Ingrese numero: ")
    if not var:
        continue

    try:
        var = int(var)
    except ValueError:
        print("Por favor, ingresa un número entero.")
        continue

  
    print("RPI: Hola arduino, te envie ", var)
    time.sleep(1)

    number = readNumber()
    print("RPI: Hola arduino, recibí un digito ", number)
