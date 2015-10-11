#!/usr/bin/env python

"""
Ejemplos de uso de ciclos *while* en Python
"""
total = 0
contador = 0

print('='*10,'Segundo ejemplo con while: Promedio de notas','='*10);

# En este caso, usamos un 'ciclo infinito': la condición siempre será cierta, y sólo
# saldremos del ciclo con un break. Aquí no necesitamos la variable 'preguntar' anterior
while True:
    print('Presione sólo ENTER para terminar');
    puntaje = input("Nota " + str(contador+1) + "- Introduzca un puntaje de 0 a 100:")
    if puntaje == '':
        break
    # En caso de una cadena vacía, el resto del bloque no se ejecuta, gracias al break
    puntaje = int(puntaje)
    if puntaje >= 0 and puntaje <= 100:
        total += puntaje
        contador += 1
    else:
        print('Valor inválido')

print('Cantidad de notas introducidas:', contador)
if contador > 0:
    print('El promedio de notas obtenido es', round(total/contador, 2) )
