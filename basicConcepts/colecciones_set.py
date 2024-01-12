#           MANEJO DE SET

print("*** Manejo de Set ***")

#No hay índices (elementos no ordenados). No se pueden repetir elementos

conjunto = {"Karla", 100, "Laura", True, "Karla"}
print(f'El conjunto o Set es: {conjunto}')

#Recorrer el set
for elemento in conjunto:
    print(elemento, end= ' ')

#Buscar un elemento
print("\n")
if 100 in conjunto:
    print("El número existe en el set")
else:
    print("El número no existe en el set")

#Largo de un set:
largo = len(conjunto)
print(f'La cantidad de elementos en mi set es: {largo}')

#Eliminar un elemento del set
conjunto.remove(100)
print(f'El set después de eliminar el valor 100 es: {conjunto}')

#Agregar un elemento al set
conjunto.add("Pycharm")
print(f'El set con el nuevo elemento es: {conjunto}')