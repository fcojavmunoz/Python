
class Alumno:

    def crear(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mensaje(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")


alumno1 = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()

alumno1.crear("Noa", 8)
alumno2.crear("Ismael", 7)
alumno3.crear("Rocco", 4)


alumno1.imprimir()
alumno1.mensaje()
alumno2.imprimir()
alumno2.mensaje()
alumno3.imprimir()
alumno3.mensaje()
