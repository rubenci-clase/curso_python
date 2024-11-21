# Operadores lógicos en python

"""
Ejemplo de operadores lógicos and, or, not
En Python, los operadores lógicos and y or utilizan el concepto de cortocircuito, 
lo que significa que no siempre evalúan todas las expresiones en una cadena lógica. 
Estos operadores pueden dejar de evaluar expresiones tan pronto como se determina el resultado final
"""

# coche con gasolina, está encendido, conductor mayor de 17 años
# realiza cambios en las variables para revisar los ejemplos
gas = False
encendido = True
edad = 15

if gas and encendido:
    print("Con gasolina y encendido")

if gas or encendido:
    print("Con gasolina o encendido")

if not gas or encendido:
    print("sin gasolina o encendido")

# Como evalua esta expresión??
if gas and encendido and edad > 17:
    print("con gasolina y encendido y conductor mayor de edad")

# Como evalua esta expresión??
if encendido or gas and edad > 17:
    print("con gasolina y encendido o conductor mayor de edad")

# se evaluan las expresiones de izquierda a derecha
# se ponen parentesis para agrupar los operadores
# comparación de cortocircuito (si no se cumple la primera condición, ya no evalua las siguientes)
if gas and (encendido or edad > 17):
    print("gas and (encendido or edad > 17)")

if not gas and (encendido or edad > 17):
    print("not gas and (encendido or edad > 17)")
