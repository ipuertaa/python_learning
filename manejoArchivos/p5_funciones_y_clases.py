"""     ARCHIVO DE DEFINICIÓN DE CLASES Y FUNCIONES DEL PROYECTO
                CATÁLOGO DE PELÍCULAS   """

import os


#Función que imprime el menú
def menu():
    print(f'''Opciones:
    1. Agregar película
    2. Listar películas
    3. Eliminar catálogo de películas
    4. Salir''')


#Clase para los objetos de tipo película
class Pelicula:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Película: {self.nombre}'


#Creación de la clase para crear el catálogo de las películas
class CatalogoPeliculas:
    nombre_archivo = 'peliculas.txt'

    #Métodos de clase: se asocian a la clase misma y no a los objetos
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.nombre_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_pelicuas(cls):
        with open(cls.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('*** Listado de películas ***')
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.nombre_archivo)
        print(f'Se eliminó el archivo {cls.nombre_archivo}')
