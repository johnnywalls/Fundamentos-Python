#!/usr/bin/env python

"""
Ejemplos de uso de condicionales en Python
"""

puntaje = int(input("Introduzca puntaje de 0 a 100:"))

# Validar que el puntaje esté dentro del rango válido (0-100)
if puntaje >= 0 and puntaje <= 100:
    if puntaje >= 90:
        calificacion = 'A'
    elif puntaje >= 80:
        calificacion = 'B'
    elif puntaje >= 70:
        calificacion = 'C'
    elif puntaje >= 60:
        calificacion = 'D'
    else:
        calificacion = 'F'
else:
    calificacion = False

print('La calificacion es:', calificacion) if calificacion else print('Entrada inválida')

# La forma abreviada de if puede usarse como una expresión
mensaje = '¡'+('Felicidades' if calificacion == 'A' else 'Puedes hacerlo mejor')+'!'
print(mensaje)