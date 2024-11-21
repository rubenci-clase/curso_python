# dentro de módulo utilidades, crud
# from espacio . desde ahí salen los módulos y paquetes de esta carpeta

from ..gestion.crud import guardar


def pagar_impuestos():
    guardar()
    print("pagando impuestos")
