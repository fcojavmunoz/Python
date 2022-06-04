peso = input("Indica tu peso: ")
estatura = input("Indica tu estatura (en metros): ")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
