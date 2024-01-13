#                   CALCULADORA CON FUNCIONES

#1. Mostrar el menú con una función
#2. Solicitar los valores para la operación con una función
#3. Ejecutar la operación en otra función por separado

print("*** Calculadora en Python con funciones ***")

#Función para mostrar menú
def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Salir''')

    opcion = int(input("Seleccione una opción:"))
    return opcion

#Función para solicitar valores
def pedir_valores():
    valor1 = float(input(f'Ingrese el valor 1: '))
    valor2 = float(input(f'Ingrese el valor 2: '))
    return valor1, valor2


#Función para ejecutar la operación
def ejecutar_operacion(opcion, salir):
    #Verificar si se desea hacer una operación:
    if opcion != 5:
        # Desempaquetar la tupla
        valor1, valor2 = pedir_valores()


    if opcion == 1:
        print(f'El resultado de la SUMA es: {valor1 + valor2}')

    elif opcion == 2:
        print(f'El resultado de la RESTA es: {valor1 - valor2}')

    elif opcion == 3:
        print(f'El resultado de la MULTIPLICACIÓN es: {valor1 * valor2}')

    elif opcion == 4:
        print(f'El resultado de la DIVISIÓN es: {valor1 / valor2}')

    elif opcion == 5:
        print("Saliendo del programa")
        salir = True

    else:
        print("Opción inválida")

    return salir
    #Si se modifica salir durante la función, cambia. De lo contrario se queda con el
    #valor con el que se llamó a la función

#   Código principal

salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)