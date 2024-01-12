#               MANEJO DE DICCIONARIOS

""" En un diccionario se almacenan elementos en forma de llave-valor
    A través de la llave se puede acceder al valor
    No se pueden duplicar los elementos de un diccionario: si se agregan varias
    definiciones para una misma llave, automáticamente se conserva la última"""

print("*** Manejo de diccionarios ***")

diccionario = {"Nombre": "Carlos Mario", "Apellido": "Cervantes",
               "Edad": 32}

print(f'El diccionario es: {diccionario}')

#Acceder a los elementos de un diccionario usando la llave
print(f'Nombre: {diccionario["Nombre"]}')
#Si se usa comilla simple externa, se debe usar comilla doble interna (o al contrario)

#También se puede usar el método get
print(f'Edad: {diccionario.get("Edad")}')

#Largo de un diccionario: 1 elemento = clave + valor
print(f'El largo del diccionario es: {len(diccionario)}')

#Agregar un nuevo elemento (se agregan al final)
diccionario["Telefono"] = 123647823
print(f'Diccionario modificado: {diccionario}')

#Obtener una lista de las llaves del diccionario:
print(f'Las llaves del diccionario son: {diccionario.keys()}')

#Obtener una lista con los valores del diccionario
print(f'Los valores del diccionario son: {diccionario.values()}')

#Obtener los elementos del diccionario (items) --> obtengo una lista de tuplas
print(f'Los elementos del diccionario son: {diccionario.items()}')

#Revisar si existe una llave en el diccionario
buscar = "Nombre"
if buscar in diccionario:
    print(f'La llave {buscar} sí existe en el diccionario')
else:
    print(f'La llave {buscar} no existe en el diccionario')

#Si se quiere modificar el valor asociado a una llave
diccionario["Edad"] = 10
print(f'La edad acualizada es: {diccionario.get("Edad")}')

#Eliminar un elemento de un diccionario
diccionario.pop("Telefono")
print(f'El diccionario sin teléfono es: {diccionario}')

#Recorrer las llaves de un diccionario:
for llave in diccionario.keys():
    print(llave, end=' - ')

#Recorrer los valores de un diccionario:
print("\n")
for valor in diccionario.values():
    print(valor, end=' - ')

#Recorrer los elementos de un diccionario como tupla (se pueden ignorar paréntesis)
print("\n")
for llave, valor in diccionario.items():
    print(f'Llave: {llave}, valor: {valor}')

#Limpiar el diccionario
diccionario.clear()
print(f'El diccionario limpio es: {diccionario}')

