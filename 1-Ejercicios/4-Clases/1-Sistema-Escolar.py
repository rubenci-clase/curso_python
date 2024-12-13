class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {}

    def inscribir(self, materia):
        self.materias[materia.nombre] = None

    def asignar_calificacion(self, materia, calificacion):
        if materia.nombre in self.materias:
            self.materias[materia.nombre] = calificacion
        else:
            print(f"{self.nombre} no está inscrito en {materia.nombre}")

    def promedio(self):
        calificaciones = [cal for cal in self.materias.values() if cal is not None]
        if calificaciones:
            return sum(calificaciones) / len(calificaciones)
        return 0


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def asignar_materia(self, materia):
        self.materias.append(materia)

    def enseñar(self, estudiante, materia):
        if materia in self.materias:
            estudiante.inscribir(materia)
        else:
            print(f"{self.nombre} no enseña la materia {materia.nombre}")


class Materia:
    def __init__(self, nombre):
        self.nombre = nombre


# Comprobación
estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("Ana")

profesor = Profesor("Dr. Pérez")

matematica = Materia("Matemáticas")
historia = Materia("Historia")

profesor.asignar_materia(matematica)
profesor.asignar_materia(historia)

profesor.enseñar(estudiante1, matematica)
profesor.enseñar(estudiante1, historia)
profesor.enseñar(estudiante2, matematica)

estudiante1.asignar_calificacion(matematica, 8)
estudiante1.asignar_calificacion(historia, 7)
estudiante2.asignar_calificacion(matematica, 9)

print(f"Promedio de {estudiante1.nombre}: {estudiante1.promedio()}")
print(f"Promedio de {estudiante2.nombre}: {estudiante2.promedio()}")