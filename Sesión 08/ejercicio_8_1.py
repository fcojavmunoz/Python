file = open('prueba_python.txt', 'w')
file.write('El archivo se ha creado con éxito\n')
file.close()

file = open('prueba_python.txt', 'r+')
file.readline()
file.write('Texto añadido al ejecutar el archivo ejercicio_8_1.py\n')

file.seek(0)
print(file.read())
file.close()