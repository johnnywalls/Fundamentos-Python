#!/usr/bin/env python

"""
Ejemplos de manejo de excepciones
"""

def mostrar_archivo_numerado(nombrearchivo):
    '''Lee y muestra por pantalla un archivo de texto plano, numerando sus líneas'''

    # Colocamos dentro del bloque try las instrucciones susceptibles de causar
    # las excepciones que queremos 'atrapar'
    try:
        # Abrir archivo para lectura (modo predeterminado)
        print('Abriendo archivo', nombrearchivo)
        with open(nombrearchivo) as archivo:
            num = 0
            for linea in archivo:
                num += 1
                print('{:03d}: {:<80s}'.format( num, linea.rstrip() ) )
    except FileNotFoundError:
        print('No se encontró el archivo', nombrearchivo)
    except PermissionError:
        print('No tiene privilegios suficientes para abrir el archivo', nombrearchivo)
    # El tipo de excepción más genérico se coloca al final, para capturar las excepciones
    # que no hayan sido interceptadas por los bloques 'except' anteriores
    except Exception as e:
        print('No se pudo abrir el archivo', nombrearchivo, type(e), e)
    finally:
        if 'archivo' in locals():
            # Cerrar archivo al finalizar
            print('Cerrando archivo', nombrearchivo)
            archivo.close()

import sys, math

archivo_lectura = sys.argv[0] if len(sys.argv) == 1 else sys.argv[1]

mostrar_archivo_numerado(archivo_lectura)

def es_entero(cadena):
    '''Determina si el valor dado de una cadena corresponde a un número entero'''
    try:
        num = int(cadena)
        return True
    except ValueError:
        return False

def es_natural(cadena):
    '''Determina si el valor dado de una cadena corresponde a un número natural'''
    try:
        num = int(cadena)
        return num >= 0
    except ValueError:
        return False

x = input('Introduzca un número entero para calcular su factorial:')

if es_natural(x):
    print(x+'! =', math.factorial( int(x) ) )
else:
    print('No se puede calcular el factorial')

# También podríamos colocar directamente:
try:
    import math # si no se encuentra o se escribe mal el módulo, se genera ImportError
    x = int(input('Introduzca un número entero para calcular su factorial:'))
    # Además de capturar excepciones, también podemos 'generarlas'. Ej: no permitiremos
    # el cálculo del factorial para los números mayores que 100
    if x > 100:
        raise ValueError('El número máximo permitido para el cálculo es 100')

    # Nótese que no es necesario colocar la siguiente instrucción dentro de 'else'
    print(str(x)+'! =', math.factorial(x) ) # si se omite el str, se genera un TypeError
except ValueError as e:
    print('Valor inválido para cálculo de factorial:', e)
except TypeError:
    print('Tipo de dato inválido para cálculo de factorial')
except ImportError:
    print('No se pudo importar el módulo de funciones matemáticas')
except Exception as e:
    print('Error:',type(e),e)

