from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


fordfiesta = Vehiculo("Rojo", "5")
print(fordfiesta)

file = open('vehiculo.txt', 'w+b')


dump(fordfiesta, file)

file.seek(0)
nuevo_fordfiesta = load(file)

print(nuevo_fordfiesta)
file.close()