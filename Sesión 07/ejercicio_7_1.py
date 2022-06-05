from operaciones import * #importar operaciones

a, b, c, d = (20, 14 , 7, 19)

print("{} + {} = {}".format(a, b, suma(a, b)))
print("{} - {} = {}".format(b, d, resta(b, d)))
print("{} * {} = {}".format(b, b, multiplicar(b, b)))
print("{} / {} = {}".format(a, c, division(a, c)))