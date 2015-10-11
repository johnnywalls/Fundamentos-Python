#!/usr/bin/env python

"""
Ejemplos de uso de ciclos *while* en Python
"""
total = 0
contador = 0
preguntar = True

print('='*10,'Primer ejemplo con while: Promedio de notas','='*10);

while preguntar:
    print('Presione sólo ENTER para terminar');
    puntaje = input("Nota " + str(contador+1) + "- Introduzca un puntaje de 0 a 100:")
    if puntaje == '':
        preguntar = False
    else:
        puntaje = int(puntaje)
        if puntaje >= 0 and puntaje <= 100:
            total += puntaje
            contador += 1
        else:
            print('Valor inválido')
else:
    print('Cantidad de notas introducidas:', contador)
    if contador > 0:
        print('El promedio de notas obtenido es', round(total/contador, 2) )
