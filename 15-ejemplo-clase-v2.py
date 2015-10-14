#!/usr/bin/env python

"""
Ejemplo de definición básica de clase, representando personajes de una popular
serie animada
"""

class Personaje:
    '''Personajes de una serie animada'''

    __version__='0.2'

    '''
    Este es un atributo de la clase (lo que llamaríamos una propiedad estática). Además,
    lo declaramos como "privado", con lo que damos a entender que su uso debería ser interno
    en nuestra clase. Lo utilizaremos para contar las instancias (objetos) de personajes
    que vayamos creando
    '''
    __contador = 0

    def __init__(self, nombre, apellido='Simpson', color='Amarillo', edad=None):
        '''
        Esta definición mantiene los mismos tres atributos como parámetros en el constructor,
        y agrega uno nuevo: la edad
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.color = color
        self.edad = edad
        type(self).__contador += 1
        if type(self).__contador == 1:
            print('*** Inicio de la escena ***')

    def __str__(self):
        '''Representación en cadena del personaje, en este caso, su nombre completo'''
        return ' '.join([self.nombre,self.apellido])

    def hablar(self, mensaje):
        '''Mostrar un diálogo atribuido al personaje'''
        print(self.nombre,'dice:\t', mensaje)

    def saludar(self):
        '''Un diálogo estándar del personaje'''
        self.hablar('Hola, soy '+str(self)+' y soy de color '+self.color)

    # Se utiliza el decorador @property para indicar que queremos que el método que sigue
    # sea interpretado por la clase como una propiedad de sus objetos (el equivalente en
    # Python a un método 'get')
    @property
    def edad(self):
        # Usamos una propiedad privada para el valor interno
        if self.__edad is None:
            return 'Sin edad :)'
        else:
            return str(self.__edad) + ' años'

    # Análogamente, utilizamos el decorador @*.setter para indicar que el método que sigue
    # será invocado al intentar asignar un valor a la propiedad especificada (el equivalente
    # en Python de un método 'set')
    @edad.setter
    def edad(self, edad):
        if type(edad) == int:
            if edad < 0: # La edad no debe ser negativa, colocar a 0 en ese caso
                self.__edad = 0
            elif edad > 100: # Establecemos la edad máxima en 100
                self.__edad = 100
            else:
                self.__edad = edad
        else:
            self.__edad = None

    # En este método estático retornamos el contador de objetos, de esta forma
    # podemos ver el contador pero no modificarlo manualmente desde fuera de la clase
    @staticmethod
    def PersonajesEnEscena():
        '''Cantidad de personajes que han aparecido en escena'''
        return Personaje.__contador

    # Ejemplo de 'destructor'
    def __del__(self):
        type(self).__contador -= 1
        if type(self).__contador == 0:
            print('*** Fin de la escena ***')

if __name__ == "__main__":
    p1 = Personaje('Homero')
    p1.saludar()

    p2 = Personaje(edad=40,color='Marrón',nombre='Apu',apellido='Nahasapeemapetilon')
    p2.hablar('Hola, Homero. ¿Cuántos años tienes?')

    p1.hablar( p1.edad + '. ¿Y tú?')
    p2.hablar( p2.edad )

    p2.hablar('¿Quieres dos cajas de donas, como siempre?')
    p1.hablar('Pero, ¡alguien se ha llevado todas las donas!')

    p3 = Personaje(nombre='Bart')
    p3.hablar('¡Ay caramba!')

    print('Han aparecido',Personaje.PersonajesEnEscena(),'personajes')

    print('Bart sale corriendo...')
    del p3 # también podríamos hacer p3 = None
    print('Quedan',Personaje.PersonajesEnEscena(),'personajes')

    p1.hablar('¡Pequeño demonio!')
