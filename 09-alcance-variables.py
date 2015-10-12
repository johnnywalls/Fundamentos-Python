#!/usr/bin/env python

"""
Ejemplos de alcance de variables
"""

def f():
    s = 42
    print('Estoy en la función f')
    print(s)

# En este primer ejemplo, la variable 's' dentro de la función f es una variable local,
# y no afecta el valor de 's' fuera de ella
s = '¡Hola, mundo!'
f()
print(s)

def g():
    print('Estoy en la función g')
    print(s)
    #s = 3.14 # Esta instrucción ocasionaría un error en tiempo de ejecución
    if s:
        t = 'Adiós...' # la variable t existe sólo dentro de la función g
        print(t)

    print(t) # aunque se definió dentro del bloque if, aún podemos usar 't' dentro de 'g'

g()
print(s)
#print(t) # Esto ocasionaría un error en tiempo de ejecución: 't' existe sólo dentro de 'g'

def h():
    global s # De este modo podemos acceder a la variable 's' de alcance global
    print('Estoy en la función h')
    print(s)
    s = 3.14 # Esta instrucción modifica la variable global de 's'

h()
print(s)

import math

def circunferencia(radio):
    longitud = 2 * math.pi * radio
    radio = 0 # El parámetro se comporta como una variable local en la función.
              # Para valores 'sencillos' como cadenas, números o tuplas, el valor del
              # parámetro en el ámbito de donde se llama a la función no se ve alterado.
              # En caso de otros tipos, como listas, diccionarios y otros objetos, es
              # posible afectar el valor del parámetro dentro de la función y que dicho
              # cambio sea visible fuera de ella
    return longitud

r = 10
print(circunferencia(r))
print(r)

