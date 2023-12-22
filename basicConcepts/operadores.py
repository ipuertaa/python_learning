#       ASIGNACIÓN DE VALORES MULTIPLES

a = 5
b = 10
print(f'El valor de a es: {a} y el valor de b es: {b}')

a, b, c = 10, 5, 14
print(f'Ahora el valor de a es: {a}, el valor de b es: {b} y el valor de c es: {c}')

# Asignación del mismo valor a varias variables
#a = b = c = 100
#print(f'Ahora el valor de a es: {a}, el valor de b es: {b} y el valor de c es: {c}')


#       OPERADORES DE ASIGNACIÓN COMPUESTOS

#a = a + b ->Ya no necesito variables de resultado, sino que el resultado se guarda en b
a += b
print(f'El operador compuesto de a+=b es: {a}')


#a = a - b
a -= b
print(f'El operador compuesto de a-=b es: {a}')

#b = b * a
print(f'El valor de a es: {a}')
print(f'El valor de b es: {b}')
b *= a
print(f'El operador compuesto de b*=a es: {b}')


#       OPERADORES DE COMPARACIÓN
a, b = 7, 5
print(f'El valor de a es: {a}')
print(f'El valor de b es: {b}')

#Operador igualdad ==       Regresa un valor lógico(True/False)
result = a == b
print(f'La igualdad es: {result}')

#Operador diferente !=
result = a != b
print(f'La operación a != b es: {result}')

#Operador mayor que >
result = a > b
print(f'La operación a > b: {result}')

#Operador mayor que >=
result = a >= b
print(f'La operación a >= b: {result}')


