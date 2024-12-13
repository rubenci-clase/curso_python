class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.nombre}: {estado}"


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)

    def progreso(self):
        tareas_completadas = len([tarea for tarea in self.tareas if tarea.completada])
        total_tareas = len(self.tareas)
        if total_tareas == 0:
            return 0
        return (tareas_completadas / total_tareas) * 100

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)


class ListaDeTareas:
    def __init__(self):
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_proyectos(self):
        for proyecto in self.proyectos:
            print(f"Proyecto: {proyecto.nombre} - Progreso: {proyecto.progreso():.2f}%")
            proyecto.mostrar_tareas()


# Comprobación
tarea1 = Tarea("Tarea 1", "Descripción de la tarea 1")
tarea2 = Tarea("Tarea 2", "Descripción de la tarea 2")
tarea3 = Tarea("Tarea 3", "Descripción de la tarea 3")

proyecto = Proyecto("Proyecto de Ejemplo")
proyecto.agregar_tarea(tarea1)
proyecto.agregar_tarea(tarea2)
proyecto.agregar_tarea(tarea3)

tarea1.marcar_completada()
tarea2.marcar_completada()

lista_tareas = ListaDeTareas()
lista_tareas.agregar_proyecto(proyecto)

# Mostrar los proyectos y el progreso
lista_tareas.mostrar_proyectos()
