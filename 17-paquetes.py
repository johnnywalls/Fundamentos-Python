#!/usr/bin/env python

'''
En este ejemplo, hemos organizado las definiciones de clases en un paquete
'''

# Importamos todas las clases disponibles en nuestro módulo de personajes
from ejemplos.simpsons.personajes import *

p1 = TrabajadorPlanta('Homero')
p1.saludar()

p2 = Personaje(nombre='Lisa')
p2.hablar('Hola, papá. ¿Por qué me llamas a esta hora?')

p1.hablar('Pues no estaba haciendo nada en el trab...')

p3 = TrabajadorPlanta(nombre='Carl',
                      apellido='Carlson',
                      color='Marrón',
                      edad=40,
                      departamento='Seguridad Industrial')
p3.hablar('¡Homero! ¡Hay una alarma en tu tablero! ¡Una fuga del reactor!')

p1.hablar("¡D'oh!")

p3.hablar("Apenas tengo " + p3.edad + '. ¡Soy muy joven para morir!' )

p2.hablar('¿Quién está allí?')
p3.saludar()

print('Personaje(s):',Personaje.PersonajesEnEscena())
print('Trabajador(es):',TrabajadorPlanta.PersonajesEnEscena())
