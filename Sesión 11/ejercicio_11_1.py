"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:

la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido
que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import sqlite3

db_conn = sqlite3.connect('alumnos.db')
db_cursor = db_conn.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Lukas', 'Kimmig')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Andreas', 'Klummp')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Ronja', 'Brede')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Haziz', 'Berisha')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Hansel', 'Gretel')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Elke', 'Meier')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Alejandro', 'Cafelitos')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Niko', 'Niebert')")

db_conn.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Ronja'")

filas = db_cursor.fetchall()

print(filas)



db_cursor.close()
db_conn.close()