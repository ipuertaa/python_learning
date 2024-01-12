#           MANEJO DE TUPLAS

print("*** Manejo de tupas ***\n")

nombres = ('Karla', 'Juan', 'Laura')
print(f'La tupla nombres es: {nombres}')

#Tupla con diferentes tipos de variables
#Nota: los paréntesis se pueden omitir:
tupla_heterogenea = 100, True, "Ivonne"
print(f'La tupla de diferntes tipos de variables es: {tupla_heterogenea}')

#Tupla con un sólo elemento
tupla_mono = 100,
print(f'La tupla con un sólo elemento es: {tupla_mono}')

#Recorrer los elementos de una tupla
for nombre in nombres:
    pass
#Si quiero omitir un bloque de código --> pass
#    print(nombre, end = ' ')

numeros = 100, 200, 300, 400, 500

#Recuperar un índice de la tupla:
print(f'Para el índice 0 el valor es: {numeros[0]}')

#También los índices pueden ser negativos
print(f'Para recuperar el último elemento usando índices negativos: {numeros[-1]}')

