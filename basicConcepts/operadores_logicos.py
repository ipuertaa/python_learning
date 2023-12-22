#               OPERADORES LÓGICOS

# condicion1 = False
# condicion2 = True
#
# #                                   Operación AND
# resultado = condicion1 and condicion2
# print(f'El resultado de la operación AND es: {resultado}')
#
#
# #                                   Operación OR
# resultado = condicion1 or condicion2
# print(f'El resultado de la operación OR es: {resultado}')
#
#
# #                                   Operación NOT
# resultado = not condicion1
# print(f'El resultado de not1 es: {resultado}')

"""Esto es un bloque de código en python"""

#               CICLOS

#                                   Ciclo WHILE

contador = 0

while contador < 5:
    contador += 1
    print(f'El valor del contador es: {contador}')

print(f'Ciclo finalizado')


#                                   Ciclo FOR

cadena = "Hola mundo"

for letra in cadena:
    #Se usa el end= para que se imprima en un mismo renglón
    print(letra, end=' ')

print('\n')

for i in range(1, 5):
    print(i)
    #Para que se tome el 5, debería ser (1,6)
