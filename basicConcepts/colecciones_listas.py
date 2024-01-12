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

#Reasignar valores a la lista
numeros = [100, 200, 300, 400, 500]

#Recuperar una parte de la lista --> crear una sublista  lista[indice_inicio: indice_final-1]
valores_recuperados = numeros[0:3]
#Recuperando del indice 0 al 2, no se toma el último
print(f'La sublista usando los dos índices es: {valores_recuperados}')

#Recuperar una sublista indicando índice final. Si no se especifica el inicio empieza desde cero
valores_recuperados = numeros[:2]
print(f'La sublista usando sólo el índice final es: {valores_recuperados}')

#Recuperar una sublista indicando el índice de inicio. Si se omite el final se va hasta el final de la lista
valores_recuperados = numeros[2:]
print(f'La sublista usando sólo el índice inicial es: {valores_recuperados}')

#Realizar una copia de una lista --> terminan siendo dos listas totalmente diferentes en memoria
copy_list = numeros[:]
print(f'La lista copiada es: {copy_list}')

print("\n")

print("*** Métodos para trabajar con listas ***\n")

#Conocer el largo de la lista (cantidad de elementos)
largo_lista = len(numeros)
print(f'El largo de la lista es: {largo_lista}')

#Agregar un nuevo elemento al final de la lista:
numeros.append(600)
print(f'La lista con el nuevo valor al final es: {numeros}')

#Insertar nuevos elementos en el índice deseado
numeros.insert(2, 50)
print(f'La lista con el nuevo valor en el índice 2 es: {numeros}')

#Eliminar un valor de una lista (elimina el primer valor que se encuentre de izquiera a derecha)
numeros.remove(600)
print(f'La lista con el valor 600 eliminado: {numeros}')

#Concatenar lista
nueva_lista = numeros + copy_list
print(f'La nueva lista concatenada es: {nueva_lista}')

#Eliminar un elemento por índice --> del lista[indice a remover]
del numeros[3]
print(f'La lista removiendo el índice 3 es: {numeros}')

#Eliminar una lista completa --> Asignar una lista vacía a todos los elementos
numeros[:] = []
print(f'Al eliminar todos los elementos de la lista: {numeros}')

#Eliminar por completo la variable
del numeros

