import time
import datetime

class Sensor:
    def leer_temperatura(self):
        # Aquí iría el código para leer la temperatura del sensor
        # Para este ejemplo, simplemente devolveremos una temperatura aleatoria
        import random
        return 20 + random.random() * 10

class Reloj:
    def obtener_hora_actual(self):
        return datetime.datetime.now()

class Calculadora:
    def calcular_promedio(self, datos):
        return sum(datos) / len(datos)

class RegistroDeTemperaturas:
    def __init__(self):
        self.sensor = Sensor()
        self.reloj = Reloj()
        self.calculadora = Calculadora()
        self.datos_de_temperatura = []

    def adquirir_dato_de_temperatura(self):
        temperatura = self.sensor.leer_temperatura()
        timestamp = self.reloj.obtener_hora_actual()
        self.datos_de_temperatura.append(temperatura)
        print(f'{timestamp}: {temperatura}')

    def almacenar_promedio_de_temperatura(self):
        promedio = self.calculadora.calcular_promedio(self.datos_de_temperatura)
        timestamp = self.reloj.obtener_hora_actual()
        with open('promedios.txt', 'a') as f:
            f.write(f'{timestamp}: {promedio}\n')
        print(f'Promedio almacenado: {promedio}')
        self.datos_detemperatura = []

registro = RegistroDeTemperaturas()
