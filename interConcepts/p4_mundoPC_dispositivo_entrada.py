#CREACIÓN DE LA CLASE DISPOSITIVO ENTRADA

class DispositivoEentrada:
    #Constructor de la clase
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada


#CREACIÓN DE LA CLASE RATON
class Raton(DispositivoEentrada):
    #Atributo de clase
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        #Asigno ID
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        #Llamo al metodo init de DispoEntrada
        #super() indica que es del objeto tipo raton (el que lo llama)
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'  Id: {self.id_raton}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}'


#CREACIÓN DE LA CLASE TECLADO:
class Teclado(DispositivoEentrada):
    #Atributo de clase
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        #Asigno ID
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        #Llamo al init del padre
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}'