#USO DE PROGRAMACIÓN ORIENTADA A OBJETOS PARA MEJORAR EL PROYECTO

""" CREACIÓN DE LA CLASE SNACK:
    Esta es la clase para crear objetos tipo Snack"""


class Snack:
    #atributo de clase
    contador_snacks = 0

    #inicializar con el constructor
    def __init__(self, nombre, precio):
        Snack.contador_snacks += 1
        self.id = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Id: {self.id} Producto: {self.nombre} Precio: ${self.precio}'


""" CREACIÓN DE LA CLASE SNACKS
    Esta clase posee un atributo de clase que corresponde a la lista con
    los objetos Snack disponibles. 
    También está el método para añadir otro snack al inventario 
    
    Lo que está pasando en cada proceso es:
    lista_snacks: es una lista que contiene todos los objetos tipo Snack
    que se crearon (con los atributos de nombre y precio)
    agregar_snacks: se añade a la lista de snacks el objeto snack 
    que se ingresa al método
    
    __str__: crea una lista vacía para la impresión
    recorre todos los objetos tipi snack en la lista_snacks
    por cada uno de ellos, guarda en la lista de impresión
    un salto de linea seguido del atributo.__str__ del objeto en 
    cuestion.
    Se imprime la lista de impresion
    """


class Snacks:
    #Lista de los elemenentos tipo snack
    lista_snacks = [Snack("Papas", 70),
                    Snack("Refresco", 50),
                    Snack("Sanduche", 120)]

    def agregar_snacks(self, snack):
        #Por consola se pedirá al usuario que indique el objeto snack
        Snacks.lista_snacks.append(snack)

    def __str__(self):
        snacks_str = ''
        for snack in Snacks.lista_snacks:
            snacks_str += '\n' + snack.__str__()
        return f''' *** Snacks en inventario *** {snacks_str}'''
