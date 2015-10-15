#!/usr/bin/env python

"""
Ejemplo de herencia en clases de Python, representando personajes de una popular
serie animada
"""

class Personaje:
    '''Personajes de una serie animada (misma definición de lección sobre Clases)'''

    __version__='0.3'

    '''
    Este es un atributo de la clase (lo que llamaríamos una propiedad estática). Además,
    lo declaramos como "protegido", con lo que damos a entender que su uso debería ser interno
    en nuestra clase y sub-clases. Lo utilizaremos para contar las instancias (objetos) de
    personajes que vayamos creando
    '''
    _contador = 0

    def __init__(self, nombre, apellido='Simpson', color='Amarillo', edad=None):
        '''
        Esta definición mantiene los mismos tres atributos como parámetros en el constructor,
        y agrega uno nuevo: la edad
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.color = color
        self.edad = edad
        type(self)._contador += 1
        if type(self)._contador == 1:
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
        return Personaje._contador

    # Ejemplo de 'destructor'
    def __del__(self):
        type(self)._contador -= 1
        if type(self)._contador == 0:
            print('*** Fin de la escena ***')

class TrabajadorPlanta(Personaje): # El nombre de la super-clase
    __version__='0.2'

    # Tenemos nuestro propio contador para la subclase
    _contador_trabajadores = 0

    def __init__(self, nombre, apellido='Simpson',
                 color='Amarillo', edad=None, departamento='No asignado'):
        '''
        En esta definición se agrega el atributo departamento
        '''
        super().__init__(nombre, apellido, color, edad)
        self.departamento = departamento
        type(self)._contador_trabajadores += 1
        Personaje._contador += 1 # Ya que un trabajador también es un personaje, lo contamos

    def __str__(self):
        '''Representación en cadena del trabajador'''
        return super().__str__() + ' (Departamento: ' + self.departamento+')'

    # Haremos una 'sobrecarga' de un método de la super-clase
    def hablar(self, mensaje):
        '''Mostrar un diálogo atribuido al personaje'''
        print('(Desde la Planta Nuclear de Springfield)')
        super().hablar(mensaje)

    # Redefinimos el método estático para hacer referencia al contador específico
    # de la sub-clase
    @staticmethod
    def PersonajesEnEscena():
        '''Cantidad de trabajadores que han aparecido en escena'''
        return TrabajadorPlanta._contador_trabajadores

    def __del__(self):
        type(self)._contador_trabajadores -= 1
        if type(self)._contador_trabajadores == 0:
            print('*** Ya no quedan trabajadores de la Planta ***')
        Personaje._contador -= 1 # Al desaparecer un trabajador, también desaparece un personaje
        super().__del__()

if __name__ == "__main__":
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

