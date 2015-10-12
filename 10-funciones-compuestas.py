#!/usr/bin/env python

"""
Ejemplos de funciones 'compuestas' y usos de funciones como tipo de dato
"""

# Las funciones también pueden ser definidas dentro de otras funciones, y ser usadas como
# un tipo de datos: parámetros, valores de retorno, etc., pueden ser también funciones
def generar_operacion(operador='+'):
    """Realizar una operación sobre dos números, mostrando la operación realizada"""
    def f(a,b):
        resultado = eval('a'+operador+'b')
        print(a,operador,b,'=',resultado)
        return resultado
    return f

suma = generar_operacion()
suma(2,3)
potencia = generar_operacion('**')
potencia(2,3)

# Las funciones pueden utilizarse para 'modificar' otras funciones (a esto se le denomina
# un 'decorador' en Python). En este caso, validar_argumento_natural recibe una función
# como parámetro y retorna otra función
def validar_argumento_natural(funcion):
    def auxiliar(x):
        if type(x) == int and x > 0:
            return funcion(x)
        else:
            print('El argumento no es válido, debe ser un entero positivo')
            return
    return auxiliar

import math

# Aquí, sólo invocamos la función disponible en el módulo math
def factorial(n):
    return math.factorial(n)

# Aquí aplicamos nuestro 'decorador', modificando la función 'factorial'
factorial = validar_argumento_natural(factorial)

print('5!=',factorial(5))
print('2.5!=',factorial(2.5))

#print('2.5!=',math.factorial(2.5)) # Directamente, se generaría un error de ejecución

# Otro ejemplo de decorador: mostrar el tiempo de ejecución de una función
def mostrar_tiempo(f):
    from time import time as reloj
    def auxiliar(x):
        inicio = reloj()
        resultado = f(x)
        fin = reloj()
        print('Tiempo de ejecución:', fin-inicio, end='| ')
        return resultado

    return auxiliar


# En Python, podemos utilizar una sintaxis abreviada para indicar un 'decorador'
@validar_argumento_natural
@mostrar_tiempo
def factorial2(n):
    return math.factorial(n)

# Lo anterior sería equivalente a definir la función factorial2 y después agregar:
# factorial2 = validar_argumento_natural(factorial2)
# factorial2 = mostrar_tiempo(factorial2)

print('5!=',factorial2(5))
print('20!=',factorial2(20))
print('50!=',factorial2(50))
print('2.5!=',factorial2(2.5))

# En el siguiente ejemplo, definimos 'al vuelo' una función de suma con la notación lambda
suma = lambda a,b : a + b
print( suma(2,3) )

# O directamente, hacer que se calcule e imprima el resultado
mostrar_suma = lambda a,b: print(a,'+',b,'=',suma(a,b))
mostrar_suma(2,3)
