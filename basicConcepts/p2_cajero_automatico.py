#                          PROYECTO 2: CAJEO AUTOMÁTICO

""" OPERACIONES A REALIZAR:
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir                """

#Variables
salir = False
saldo = 200000.00

# Mensaje de bienvenida:
print("*** BIENVENIDO AL CAJERO AUTOMÁTICO ***")

# Para que el menú se repita indefinidamente hasta que el usuario salga:
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar dinero
    3. Depositar dinero
    4. Salir 
''')
    opcion = int(input("Seleccione una opción: "))

    #Opción para consultar saldo
    if opcion == 1:
        print(f'Tu saldo es: ${saldo:.2f}\n')

    #Opción para retirar dinero
    elif opcion == 2:
        cant_retirar = int(input("Ingrese la cantidad a retirar: $"))
        if saldo >= cant_retirar:
            saldo -= cant_retirar
            print(f'''Retirando ${cant_retirar}
Su nuevo saldo es: ${saldo:.2f}\n''')
        else:
            print("Saldo insuficiente")

    #Opción para depositar dinero:
    elif opcion == 3:
        cant_depositar = int(input("Ingrese la cantidad a depositar: $"))
        saldo += cant_depositar
        print(f'Su nuevo saldo es ${saldo:.2f}\n')

    #Opción para salir:
    elif opcion == 4:
        salir = True
        print("Finalizando operación. Hasta pronto")

    #Opción inválida:
    else:
        salir = True
        print("Opción no válida. Finalizando operación. Hasta pronto")
