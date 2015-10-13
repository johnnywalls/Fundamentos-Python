#!/usr/bin/env python

"""
Ejemplos de uso y manipulación de listas
"""

# En esta lista, cada elemento será a su vez una lista
menu_desayunos =  [
    ['Cereal', 2.80],
    ['Sandwich', 3.50],
    ['Continental', 3.80],
    ['Buffet', 5.99],
]

def mostrar_menu(menu, titulo='Menú'):
    '''Mostrar las opciones del menú con formato'''
    if not type(menu)==list and len(menu)>0:
        raise ValueError('No hay opciones en el menú')
    ancho = 30
    print('~'*ancho)
    print(titulo.center(ancho,'~'))
    print('~'*ancho)
    num = 0
    print('~  {:<16s} ~ {:>6s} ~'.format('Plato','Precio'))
    # Recorremos todos los elementos de la lista
    for opcion in menu:
        num += 1
        print('~ {n:2d}-{plato:<14s} ~ {precio:6.2f} ~'.format(
            plato=opcion[0], # el nombre del plato está en la posición 0
            precio=opcion[1], # el precio del plato está en la posición 1
            n=num))
    print('~'*ancho)

def seleccion_valida(menu, sel):
    '''
    Dado un texto de selección (sel), que puede corresponder a un número de opción en el
    menú, o al nombre de un plato del mismo, buscar y retornar la opción seleccionada
    '''
    if sel.isdigit():
        # Validar por número de opción
        num_opcion = int(sel)
        if num_opcion >= 1 and num_opcion <= len(menu):
            return menu[num_opcion-1]
        else:
            raise ValueError
    else:
        # Validar por nombre de plato
        plato = sel.casefold() # 'casefold' para obviar mayúsculas/minúsculas

        # La siguiente es una operación de 'comprensión' (ing: comprehension) de listas.
        # Generamos una nueva lista con las opciones del menú que correspondan con el
        # nombre del plato dado. Ya que los platos en nuestro menú son únicos, en caso
        # exitoso debemos tener un solo resultado
        menu_seleccionado = [ opcion for opcion in menu if opcion[0].casefold() == plato ]
        if len(menu_seleccionado) == 1:
            return menu_seleccionado[0]
        else:
            raise ValueError

def seleccionar_plato(menu, selecciones):
    '''Seleccionar un plato del menú, agregando cada selección a una lista'''
    while True:
        try:
            print("Escoja su opción de menú (# o nombre). Enter para terminar:", end='')
            seleccion = input()
            if seleccion == '':
                break
            plato = seleccion_valida(menu, seleccion)
            print('¡Sale una orden de', plato[0], 'por', '{:<.2f}'.format(plato[1]), '!')
            # Agregamos la selección de plato más reciente al arreglo
            selecciones.append(plato)
        except ValueError:
            print("Opción inválida, intente de nuevo")


def mostrar_selecciones(sel, titulo='Platos Seleccionados'):
    '''Mostrar los platos seleccionados con formato'''
    if not type(sel)==list and len(menu)>0:
        raise ValueError('No hay selecciones que mostrar')
    ancho = 30
    print('~'*ancho)
    print(titulo.center(ancho,'~'))
    print('~'*ancho)
    total = 0
    print('~ {:<17s} ~ {:>6s} ~'.format('Plato','Precio'))
    for opcion in sel:
        total += opcion[1]
        print('~ {plato:<17s} ~ {precio:6.2f} ~'.format(
            plato=opcion[0],
            precio=opcion[1]))
    print('~'*ancho)
    print('~ {:<17s} ~ {:6.2f} ~'.format('Total',total))
    print('~'*ancho)


mostrar_menu(menu_desayunos, 'Desayunos')

desayunos_seleccionados = []

seleccionar_plato(menu_desayunos, desayunos_seleccionados)

mostrar_selecciones(desayunos_seleccionados)

# Acá ilustramos cómo eliminar un elemento de una lista (en este caso, el último)
print('Hubo una equivocación: deshacer el pedido más reciente...')
ultimo = desayunos_seleccionados.pop()
print('Se eliminó una orden de',ultimo[0],'por','{:<.2f}'.format(ultimo[1]))

mostrar_selecciones(desayunos_seleccionados)

print('Mostrar platos seleccionados ordenados alfabéticamente por nombre de plato')
# La función sorted devuelve una nueva lista con los elementos de una lista original
# ordenados. Las listas también tienen un método sort(), pero éste ordena y modifica
# la lista 'al vuelo'. Usamos la función sorted si no queremos modificar la lista original
# y lista.sort() en caso contrario
mostrar_selecciones(sorted( desayunos_seleccionados, key = lambda x: x[0].casefold() ))

print('Mostrar platos seleccionados ordenados por precio descendentemente')
mostrar_selecciones(sorted( desayunos_seleccionados, key = lambda x: x[1], reverse=True ))

print('¿Cuántas órdenes de Sandwich tenemos?')
# Aquí tenemos una nueva 'comprensión' (o detalle) de lista: en los platos seleccionados
# tenemos, al igual que en el menú, una lista con el nombre del plato y el precio, y en
# este caso queremos obtener una lista sólo con los nombres de platos (posición 0) para
# luego contar más fácilmente con el método lista.count()
nombres_platos_seleccionados = [ x[0] for x in desayunos_seleccionados ]
print( nombres_platos_seleccionados.count('Sandwich') )
