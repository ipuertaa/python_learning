#Importar los archivos
from p4_mundoPC_dispositivo_entrada import Teclado, Raton
from p4_mundoPC_monitor import Monitor, Computadora, Orden

#Código principal

#Computadora 1
teclado1 = Teclado("ASUS", "interna")
raton1 = Raton("ASUS", "pad táctil")
monitor1 = Monitor("ASUS", 27)
computador1 = Computadora("ASUS Vivobook", monitor1, teclado1, raton1)

#Computadora2
teclado2 = Teclado("HP", "USB")
raton2 = Raton("Genius", "inalámbrico")
monitor2 = Monitor("HP", 14)
computador2 = Computadora("MIX", monitor2, teclado2, raton2)

#Creación de la orden
lista_computadoras = [computador1, computador2]
orden_compra = Orden(lista_computadoras)

#Creación de un elemento adicional
teclado3 = Teclado("Apple", "Bluetooth")
computador3 = Computadora("Apple", monitor1, teclado3, raton2)

#Agregar a la orden de compra
orden_compra.agregar_computadora(computador3)
print(orden_compra)
