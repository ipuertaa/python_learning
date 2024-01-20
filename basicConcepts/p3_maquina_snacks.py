#                       PROYECTO DÍA 3 --> MÁQUINA DE SNAKS
from p3_maquina_snacks_POO import Snack, Snacks

#Lista donde se almacenan los productos que el cliente pide
productos = []

print("***      MÁQUINA DE SNACKS       ***")
print("Snacks disponibles: ")

#Creación del objeto tipo Snacks (la lista)
snacks_disponibles = Snacks()
print(snacks_disponibles)


#Creación de la función menu
def menu():
    print(f'''Menú:
    1. Comprar un snack
    2. Mostrar factura
    3. Agregar un nuevo snack al inventario
    4. Salir
    ''')


#Creación de la función comprar
def comprar(snacks, productos):
    id_snack = int(input("Ingrese el id del snack que desea: "))

    #Recorrer la lista de snacks a ver si el ID está disponible
    snack_encontrado = None
    for snack in snacks_disponibles.lista_snacks:
        if id_snack == snack.id:
            snack_encontrado = snack
            break

    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'{snack_encontrado} agregado a la lista de compra')

    else:
        print(f'No fue encontrado el producto de id {id_snack}')


#Creación de la función mostrar ticket
def mostrar_ticket(productos):
    ticket = f'\t *** Ticket de venta ***'
    total = 0
    for producto in productos:
        ticket += f"\n\t {producto.nombre} - ${producto.precio}"
        total += producto.precio

    ticket += f'\n\t TOTAL = ${total}'
    print(ticket)


#Creación de la función de agregar snacks
def agregar_snack(snacks):
    nombre = input("Nombre del snack: ")
    precio = int(input("Precio del snack: "))
    nuevo_snack = Snack(nombre, precio)
    Snacks.agregar_snacks(snacks,nuevo_snack)
    print(f'El snack {nuevo_snack} ha sido agregado al inventario')


#Creación de la función maquina_snacks
def maquina_snacks(snacks, ticket):
    #Snacks ahora es un objeto que contiene la lista de los disponibles
    #Ticket es donde se van a almacenar los productos
    salir = False
    while not salir:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            comprar(snacks_disponibles, ticket)

        elif opcion == 2:
            mostrar_ticket(productos)

        elif opcion == 3:
            agregar_snack(snacks)

        elif opcion == 4:
            print("Gracias por tu compra")
            salir = True

        else:
            print("Opción no válida")


#Llamar a la función
maquina_snacks(Snacks, productos)