#CREACIÓN DE LA CLASE MONITOR
class Monitor:
    #atributo de clase
    contador_monitor = 0

    def __init__(self, marca, tamanio):
        #Asignar el ID
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f'Id: {self.id_monitor} Marca: {self.marca} Tamaño: {self.tamanio}'


#Creación de la clase computadora. Tiene relación de agregación con los elementos anteriores
class Computadora:
    #atributo de clase
    contador_computadoras = 0

    #inicialización
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre} #{self.id_computadora}
        Monitor: {self.monitor} 
        Teclado: {self.teclado} 
        Raton: {self.raton}'''


#CREACIÓN DE LA CLASE ORDEN:
class Orden:
    numero_orden = 0

    #recibe una lista de computadoras
    def __init__(self, computadoras):
        Orden.numero_orden += 1
        self.id_ordenes = Orden.numero_orden
        self.lista_computadoras = computadoras
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self.lista_computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f'''Número de orden de computadoras: {self.id_ordenes} {computadoras_str}'''