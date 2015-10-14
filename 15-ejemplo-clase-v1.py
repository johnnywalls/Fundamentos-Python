#!/usr/bin/env python

"""
Ejemplo de definición básica de clase, representando personajes de una popular
serie animada
"""

class Personaje:
    '''Personajes de una serie animada'''

    __version__='0.1'

    def __init__(self, nombre, apellido='Simpson', color='Amarillo'):
        '''
        En esta definición sencilla, se pueden suministrar tres parámetros al constructor, de
        los cuales sólo el nombre es requerido, ya que se proveen valores predeterminados
        para los demás atributos
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.color = color

    def __str__(self):
        '''Representación en cadena del personaje, en este caso, su nombre completo'''
        return ' '.join([self.nombre,self.apellido])

    def hablar(self, mensaje):
        '''Mostrar un diálogo atribuido al personaje'''
        print(self.nombre,'dice:\t', mensaje)

    def saludar(self):
        '''Un diálogo estándar del personaje'''
        self.hablar('Hola, soy '+str(self)+' y soy de color '+self.color)

if __name__ == "__main__":
    p1 = Personaje('Homero')
    print('Personaje 1:', p1)
    print(type(p1))
    print(repr(p1))
    p1.saludar()

    p2 = Personaje(color='Marrón',nombre='Apu',apellido='Nahasapeemapetilon')
    p2.hablar('Hola, Homero. ¿Dos cajas de donas, como siempre?')