#                       PROYECTO DÍA 3 --> MÁQUINA DE SNAKS

print("***      MÁQUINA DE SNACKS       ***")

salir = False

snacks_disponibles = [
    {"Id": 0, "Producto": "Papitas", "Precio": 300},
    {"Id": 1, "Producto": "Refresco", "Precio": 50},
    {"Id": 2, "Producto": "Sandwich", "Precio": 130}
]

#Lista donde se almacenan los productos que el cliente pide
ticket = []
#print(f'''Snacks disponibles:
#        Id: {snacks_disponibles[0]["Id"]} -> {snacks_disponibles[0].get("Producto")} - Precio: {snacks_disponibles[0]["Precio"]}
#        Id: {snacks_disponibles[1]["Id"]} -> {snacks_disponibles[1].get("Producto")} - Precio: {snacks_disponibles[1]["Precio"]}
#        Id: {snacks_disponibles[2]["Id"]} -> {snacks_disponibles[2].get("Producto")} - Precio: {snacks_disponibles[2]["Precio"]}''')

# Optimización del código anterior:
print("Snacks disponibles: ")
for snack in snacks_disponibles:
    print(f'\tId: {snack["Id"]} '
          f'-> {snack["Producto"]}'
          f' - Precio: ${snack["Precio"]}')

def menu():
    print(f'''Menú:
    1. Comprar un snack
    2. Mostrar factura
    3. Salir
    ''')


#Uso de un while para que el disponible y el menú se vean siempre

while not salir:
    menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        snack_deseado = int(input("¿Ingrese el Id del snack deseado: "))

        if snack_deseado == 0:
            print(f'Se ha agregado a su lista de compras: {snacks_disponibles[0]}')
            ticket.append((snacks_disponibles[0].get("Producto"), snacks_disponibles[0].get("Precio")))

        elif snack_deseado == 1:
            print(f'Se ha agregado a su lista de compras: {snacks_disponibles[1]}')
            ticket.append((snacks_disponibles[1].get("Producto"), snacks_disponibles[1].get("Precio")))

        elif snack_deseado == 2:
            print(f'Se ha agregado a su lista de compras: {snacks_disponibles[2]}')
            ticket.append((snacks_disponibles[2].get("Producto"), snacks_disponibles[2].get("Precio")))

        else:
            print("Id de Snack no disponible")

    elif opcion == 2:
        total = 0
        if ticket == []:
            print("No se ha añadido ningún elemento a la lista de compra")

        else:
            print("*** Ticket de venta ***")
            for tupla in ticket:
                print(f'    {tupla[0]} - {tupla[1]}')
                total += tupla[1]
            print(f'    TOTAL DE COMPRA = ${total}')

    elif opcion == 3:
        print("Muchas gracias por su compra")
        salir = True

    else:
        print("Opción no válida")
