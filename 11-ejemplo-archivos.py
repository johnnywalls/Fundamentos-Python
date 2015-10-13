#!/usr/bin/env python

"""
Ejemplos de manejo de archivos de texto plano
"""

def mostrar_archivo_numerado(nombrearchivo):
    '''Lee y muestra por pantalla un archivo de texto plano, numerando sus líneas'''

    # Abrir archivo para lectura (modo predeterminado)
    with open(nombrearchivo) as archivo:
        num = 0
        for linea in archivo:
            num += 1
            # Damos formato comenzando con el número de línea (3 dígitos), eliminando los
            # espacios al final (esto incluye eliminar el \n del fin de cada línea)
            print('{:03d}: {:<80s}'.format( num, linea.rstrip() ) )

    # Cerrar archivo al finalizar
    archivo.close()

import sys

archivo_lectura = sys.argv[0] if len(sys.argv) == 1 else sys.argv[1]

mostrar_archivo_numerado(archivo_lectura)

def agregar_en_archivo(nombrearchivo, texto):
    '''
    Abre un archivo de texto plano y agrega texto al final del mismo, incluyendo
    la fecha y hora en que se agrega
    '''

    from time import strftime
    # Abrir archivo para agregar
    archivo = open(nombrearchivo, 'a')
    # Escribir texto en el archivo, incluyendo fecha y hora, con salto de línea al final
    archivo.write( strftime('[%Y-%m-%d %H:%M:%S] ') + str(texto) + "\n" )
    # Cerrar archivo al finalizar
    archivo.close()

archivo_escritura = 'ejemplo.txt'
agregar_en_archivo(archivo_escritura, '*'*40)
texto = input('Introduzca texto para agregar en el archivo ' + archivo_escritura + ':')
agregar_en_archivo(archivo_escritura, texto)
mostrar_archivo_numerado(archivo_escritura)
