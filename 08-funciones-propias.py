#!/usr/bin/env python

"""
Ejemplos de declaración e invocación de funciones propias
"""

def mostrar_suma(a,b):
    """Sumar dos números, mostrando la operación realizada"""
    print(a,'+',b,'=',a+b)

resultado = mostrar_suma(2,3)
print(resultado)

def mostrar_operacion(a,b,operador='+'):
    """Realizar una operación sobre dos números, mostrando la operación realizada"""
    print(a,operador,b,'=',eval('a'+operador+'b') )

mostrar_operacion(2,3)
mostrar_operacion(5,2,'*')
mostrar_operacion(5,2,operador='*')
mostrar_operacion(operador='/', b=5, a=2)


def sumar(a=0,*valores):
    """Sumar una cantidad variable de números, mostrando la operación realizada"""
    total = a
    print(a,end=' ')
    for valor in valores:
        print('+',valor,end=' ')
        total += valor
    print('=',total)
    return total

resultado = sumar(2,3)
print(resultado)
sumar(2,3,4)
sumar(1,2,3,4,5,6)
sumar()

import math
from time import time

def factorial(x):
    """Clásico ejemplo de función recursiva, el cálculo de factorial"""
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

inicio = time()
print('El factorial de 8 es', factorial(8), 'Tiempo:', time()-inicio)
inicio = time()
print('(math) El factorial de 8 es', math.factorial(8), 'Tiempo:', time()-inicio)
