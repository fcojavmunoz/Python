import math

def triangulo():
    base = int(input("Tamaño de la base: "))
    altura = int(input("Tamaño de la altura: "))
    areat = base * altura / 2
    print("El área de este triángulo es: " + str(areat))

def circulo():
    radio = int(input("?Cuánto mide el radio? (en metros cuadrados): "))
    areac = (radio * radio) * math.pi
    print("El área de este círculo es: " + str(areac) + " metros cuadrados.")

triangulo()
circulo()
