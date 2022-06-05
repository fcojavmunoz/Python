inicio = int(input("Número inicial: "))
final = int(input("Número final: "))
impares: [int] = []

while final <= inicio:
    final: int = int(input("El número final ha de ser mayor que el inicial. Indica otro número: "))
for i in range (inicio, final + 1):
    if (i % 2 != 0):
        impares.append(i)

print(f"Lista de Números impares entre {inicio} y {final}:")
print(impares)
