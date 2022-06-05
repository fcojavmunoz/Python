import math

def primo():
    n = int(input("Introduce un número entero: "))
    if n > 1:
        for i in range(2, int(n)):
            if (n % i) == 0:
                print(f"El número {n} no es primo.")
                break
            else:
                print(f"El número {n} sí es primo.")
                break
    else:
        print(f"{n} no es número primo porque no es mayor que 1.")


primo()
