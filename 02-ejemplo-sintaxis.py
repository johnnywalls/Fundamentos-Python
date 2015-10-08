#!/usr/bin/env python

"""
Este ejemplo contiene varios conceptos como funciones, ciclos, módulos, y se incluye
en este punto sólo para ilustrar la sintaxis de Python y su uso en varios editores
o interfaces de desarrollo. No te preocupes por los conceptos ahora, al terminar el
curso, los habrás dominado ;-)
"""

def factorial(x):
    """Clásico ejemplo de función recursiva, el cálculo de factorial"""
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def factorial_sin_recursion(x):
    """Cálculo de factorial sin recursión explícita"""
    resultado = 1
    for i in range(2,x+1):
        resultado *= i
    return resultado

if __name__ == '__main__':
    """Bloque principal de ejecución"""

    from timeit import timeit # Importar función desde módulo externo

    n = int(input('Introduzca un número entero:'))

    # Cantidad de repeticiones
    rep = 1000

    print('Medición de tiempo del cálculo recursivo del factorial de', n,
          'con', rep, 'repeticiones:')
    print(
        timeit('factorial(n)',
               setup = 'from __main__ import factorial, n',
               number = rep
               ))
    print('Medición de tiempo del cálculo sin recursión:')
    print(
        timeit('factorial_sin_recursion(n)',
               setup = 'from __main__ import factorial_sin_recursion, n',
               number = rep
               ))
