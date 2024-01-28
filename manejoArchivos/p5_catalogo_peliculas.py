"""      ARCHIVO PRINCIPAL DEL PROYECTO CATÁLOGO DE PELÍCULAS


"""
from p5_funciones_y_clases import menu
from p5_funciones_y_clases import Pelicula
from p5_funciones_y_clases import CatalogoPeliculas as catalogo_peliculas

print('*** Catálogo de películas ***')

opcion = None

while opcion != 4:
    try:
        menu()
        opcion = int(input("Escribe tu opción (1-4): "))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')

            #Creación del objeto de clase Pelicula
            pelicula = Pelicula(nombre_pelicula)

            #Por medio del catálogo de películas, se hacen las operaciones
            #En este caso no se están creando objetos ya que sólo hay atributos de clase
            catalogo_peliculas.agregar_pelicula(pelicula)

        elif opcion == 2:
            catalogo_peliculas.listar_pelicuas()

        elif opcion == 3:
            catalogo_peliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None

else:
    print('Saliendo del programa...')