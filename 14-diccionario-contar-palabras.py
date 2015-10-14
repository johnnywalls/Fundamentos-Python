#!/usr/bin/env python

"""
Ejemplo de uso de diccionario (estructura de datos) para contar palabras en un archivo
"""

'''
Leeremos un archivo de texto para hacer un resumen de la ocurrencia de las palabras
(cuántas veces aparece cada palabra en el texto). También agruparemos las palabras
según su cantidad de letras (longitud)
'''

# Abrir archivo para lectura
nombrearchivo = 'quijote1.txt'
with open(nombrearchivo) as archivo:
    contador = {} # diccionario para guardar ocurrencia de palabras
    grupo = {} # diccionario para agrupar palabras según su longitud
    for linea in archivo:
        palabras = linea.split() # separar línea en palabras, por espacio en blanco
        for palabra in palabras:
            palabra = palabra.lower().strip(".,") # cambiar a minúscula y quitar puntuación
            if palabra not in contador:
                contador[palabra] = 1
            else:
                contador[palabra] += 1
            # Agrupar según longitud
            longitud = len(palabra)
            if longitud not in grupo:
                grupo[longitud] = { palabra } # Usaremos un conjunto de palabras (sin repetir)
            else:
                grupo[longitud].add( palabra )

# Cerrar archivo al finalizar
archivo.close()

# Mostrar información
print('Total de palabras distintas:', len(contador))

print('Las diez palabras más comunes son:')
for palabra in sorted( contador, key = contador.get, reverse=True )[:10]:
    print('\t',palabra,':',contador[palabra],'ocurrencias')

print('Las palabras más largas son:')
for palabra in sorted( contador, key = len, reverse=True )[:10]:
    print('\t',palabra,':',len(palabra),'letras',contador[palabra],'ocurrencia(s)')

print('Las diez palabras más comunes (con más de 3 letras) son:')
for palabra in sorted( {x for x in contador if len(x)>3}, key = contador.get, reverse=True )[:10]:
    print('\t',palabra,':',contador[palabra],'ocurrencias')

print('Cantidad de palabras distintas según su cantidad de letras')
print('\t','{:6s} {:}'.format('Letras','Palabras'))
for longitud in grupo:
    print('\t','{:6d} {:7d}'.format(longitud, len(grupo[longitud]) ) )

print('Ocurrencias totales según cantidad de letras')
print('\t','{:6s} {:}'.format('Letras','Total palabras'))
for longitud in grupo:
    palabras_longitud = 0
    for palabra in grupo[longitud]:
        palabras_longitud += contador[palabra]
    print('\t','{:6d} {:7d}'.format(longitud, palabras_longitud) )

