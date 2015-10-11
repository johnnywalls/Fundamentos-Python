#!/usr/bin/env python

"""
Ejemplos de uso de ciclos *for* en Python
"""
# El caso más sencillo, iterar sobre un rango definido de valores
for n in range(5):
    print(n)

desayunos = ['Cereal','Tortilla']
print('='*10,'Menú para desayunos','='*10)
# Iterar sobre una lista para mostrar sus elementos
for opcion in desayunos:
    print(opcion)

comensales = int(input('¿Cuántos comensales desea introducir?'))
if comensales > 0:
    cantidad_cereal = 0
    cantidad_tortilla = 0
    # Iterar sobre otro rango de valores (en este caso, queremos comenzar en 1)
    for comensal in range(1,comensales+1):
        while True:
            seleccion = input('Selección del comensal #'+str(comensal)+':')
            if seleccion in desayunos:
                if seleccion == 'Cereal':
                    cantidad_cereal += 1
                elif seleccion == 'Tortilla':
                    cantidad_tortilla += 1
                break
            else:
                print('Selección inválida')
    print('Cereales:', cantidad_cereal)
    print('Tortillas:', cantidad_tortilla)

# Nota: este ejemplo puede implementarse mejor con el uso de diccionarios (estructura de
# datos conocida también en otros lenguajes como arreglos asociativos o 'hash')