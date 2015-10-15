#!/usr/bin/env python

'''
Ejemplo sencillo de acceso a base de datos PostgreSQL con DB-API (psycopg2)
'''

import psycopg2 as dbapi2

# Conectarse a una BD existente
conexion = dbapi2.connect(database="dvdrental",
                          host="127.0.0.1",
                          user="curso",
                          password="curso")

with conexion:
    # En DB-API, un "cursor" es el objeto utilizado para enviar comandos a una BD
    # (no confundir con el concepto de 'cursores' del lado del servidor de BD)
    with conexion.cursor() as cur:
        # Ejecutar un comando SQL (consulta)
        cur.execute("SELECT film_id, title FROM film WHERE title LIKE %s ORDER BY title",
                    ['%Alien%'])
        print('Películas con la palabra Alien:')
        for pelicula in cur:
            print(pelicula)

        cur.execute('INSERT INTO actor(first_name,last_name) VALUES(%(nombre)s,%(apellido)s)',
                    {'nombre': 'Marlon', 'apellido': 'Brando'})

        cur.execute("SELECT * FROM actor WHERE first_name = %s ORDER BY last_name",
                    ['Marlon'])
        actores = cur.fetchall()
        print('Actores llamados Marlon:')
        print(actores)

        conexion.commit()

        # Cerrar el cursor cuando ya no va a utilizarse
        cur.close()

    # El comportamiento predeterminado es de retornar los valores como tuplas.
    # Pero con psycopg2 podemos también obtener los valores como diccionarios
    from psycopg2.extras import DictCursor
    with conexion.cursor(cursor_factory=DictCursor) as dict_cur:
        dict_cur.execute("SELECT * FROM actor WHERE first_name = %s ORDER BY last_name",
                         ['Marlon'])
        print('{:^5s} {:30s} {:30s}'.format('#','Nombre', 'Apellido'))
        for actor in dict_cur:
            print('{:5d} {:30s} {:30s}'.format(actor['actor_id'],
                                               actor['first_name'],
                                               actor['last_name']))
        dict_cur.close()

# Cerrar la conexión
conexion.close()
