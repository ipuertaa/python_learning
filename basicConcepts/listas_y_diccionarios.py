#           COMBINAR LISTAS Y DICCIONARIOS

print("*** Listas y diccionarios ***\n")

personas = [
    {"Nombre": "Regina", "Apellido": "Flores", "Edad": 21},
    {"Nombre": "Alejandro", "Apellido": "Reyes", "Edad": 32}
]
print(personas)

#Acceder a una posición de la lista
print(f'La información de la primera persona es: {personas[0]}')

#Acceder a un valor(llave) del primer elemento
print(f'El nombre de la primera persona es: {personas[0].get("Nombre")}')
print(f'El nombre de la segunda persona es: {personas[1].get("Nombre")}')

#Recorrer los elementos de la lista (cada elemento es un diccionario)
for i, persona in enumerate(personas):
    print(f'Persona {i}: {persona}')