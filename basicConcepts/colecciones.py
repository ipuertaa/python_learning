#           COLECCIONES EN PYTHON

"""
Una colección permite agrupar datos en una misma variable
Se pueden almacenar cualquier tipo de datos, incluso colecciones

Tipos de colecciones en pyhton:
- Lista: se puede modificar el valor de los elementos, añadir, eliminar, etc
- Tupla: es una lista a la que no se le pueden cambiar ninguno de los elementos
- Set: los elementos no guardan ningún orden. No tienen elementos duplicados
- Diccionario:  almacena llaves y a cada llave se le asigna un valor. Los elementos
    están ordenados y es posible modificarlos

"""


#       LISTAS EN PYTHON
print("*** Listas en python ***\n")

nombres = ["Karla", "Juan", "Laura"]
print(f'La lista de nombres es: {nombres} \n')

lista_heterogenea = [100, True, "Isa"]
print(f'La lista heterogenea es {lista_heterogenea}\n')

numeros = [100, 200, 300, 400, 500]
print(f'La lista de números es: {numeros}\n')

#Como recorrer elementos de una lista
for elemento in nombres:
    print(elemento, end=' - ')

#Recuperar elementos de una lista mediante su indice
print(f'\n\nAsí se pueden recuperar posiciones determinadas: {numeros[0]}\n')

#Modificar elementos de una lista
numeros[0] = 1
print(f'La lista de números modificada es: {numeros}\n')

#Preguntar si un valor existe en la lista
buscar = 300
if buscar in numeros:
    print(f'Si existe {buscar} en la lista')
else:
    print(f'No existe {buscar} en la lista')

#Recuperar el indice de cierto elemento en la lista
indice = numeros.index(300)
print(f'El índice es {indice}')

