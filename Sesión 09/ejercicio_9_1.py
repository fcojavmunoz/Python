lista = input("Introduce países separados por comas:\n")

paises = [pais for pais in lista.split(",")]

print(",".join(sorted(list(set(paises)))))