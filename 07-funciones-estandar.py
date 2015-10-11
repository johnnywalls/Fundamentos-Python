#!/usr/bin/env python

"""
Ejemplos de uso de funciones estándar
"""

# Importar todas las funciones y objetos del módulo math
from math import *

# Importar las funciones clock y sleep del módulo time
from time import time as reloj, sleep

# Usar los módulos random y sys, sin importar explícitamente ninguna función
import random, sys

# En sys.argv encontramos los parámetros de línea de comandos suministrados
# al ejecutar el programa. Al no haber importado ninguna función u objeto explícitamente
# desde random o sys, necesitamos invocarlos con una referencia completa (modulo.xxx)
if len(sys.argv) > 1:
    p = sys.argv[1]
    print('Generando permutación aleatoria de %s...' % p)
    # Simular porcentaje de avance
    for i in range(11):
        # sleep (del módulo time) pausa la ejecución del programa por n segundos
        sleep(random.random())
        # sys.stdout.write (escribir a la salida estándar del sistema) es otra manera
        # de mostrar resultados en pantalla, además de print()
        sys.stdout.write("\r%d%%" % (i*10) )
    print()
    # random.sample genera permutaciones aleatorias de elementos
    # Usamos join() para unir elementos en una cadena
    print('Una permutación aleatoria es', ''.join(random.sample(p, len(p))))
else:
    n = random.randint(1,100)
    print('He generado un número entero aleatorio entre 1 y 100')
    # Invocamos a time() del módulo time usando el alias reloj() con el cual la importamos
    inicio = reloj()
    while True:
        resp = input('Adivina el número o presiona sólo ENTER si te das por vencido:')
        if resp == '':
            print('El número a adivinar era', n)
            print('Tardaste', reloj()-inicio, 'segundos en darte por vencido')
            break

        # isdigit() es una función de las cadenas de texto en Python
        if resp.isdigit():
            resp = int(resp)
            if resp >= 0 and resp <= 100:
                if resp == n:
                    print('!Adivinaste en', reloj()-inicio, 'segundos!')
                    break
                elif resp > n:
                    print('Muy arriba')
                else:
                    print('Muy abajo')
            else:
                print('Número inválido')
        else:
            print('Respuesta inválida')

    # Las funciones factorial y sqrt están incluidas en el módulo math, del cual importamos todo
    print('El factorial de', n, 'es', factorial(n))
    print('La raíz cuadrada de', n, 'es', sqrt(n))
