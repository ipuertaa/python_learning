#               HERENCIA EN PYTHON

""" Puedo tener clases (hijas) que heredan características de otra
    clase (padre)"""


#Definición de la clase padre:
class Animal:
    def comer(self):
        print("Como varias veces al día")

    def dormir(self):
        print("Duermo muchas horas")


#Definición de la clase hija -> hace referencia a la clase padre:
class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")

    #SOBREESCRITURA DE MÉTODOS
    #Modificar el método heredado desde las clases hijas
    def dormir(self):
        print("Un perro sólo duerme 10 horas al día")


class Gato(Animal):
    def dormir(self):
        print("Un gato duerme todo el día")


#Código principal:
print("*** Herencia en python ***")

#Creación del objeto clase padre
print("Clase padre: soy un animal cualquiera")
animal1 = Animal()
#Métodos a los que puedo acceder
#En este caso el método cómer es el original (sin reescribir)
animal1.comer()
animal1.dormir()

#Creación del objeto clase hija
print("\nClase hija: soy un perro")
perro1 = Perro()
#Métodos a los que puedo acceder
#En este caso el método dormir que se ejecuta es el reescrito
perro1.comer()
perro1.hacer_sonido()
perro1.dormir()

#Creación del objeto clase hija
print("\nClase hija: soy un gato")
gato1 = Gato()
gato1.comer()
gato1.dormir()

""" En este caso, se realizó polimorfismo con el método dormir: 
    originalmente estaba en el padre y se modificó en ambos hijos 
    independientemente"""

""" NOTA: cuando al crear una clase los paréntesis se dejan vacíos
    por defecto es un heredero de la clase object, pero eso no se 
    debe escribir literalmente
    Por ejemplo __init__ es un método de la clase object
    En general los métodos mágicos son métodos de esa clase"""


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #Sobreescribir el método __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        dir_memoria = {super.__str__(self)}'''
        # __str__ por default imprime la dirección de memoria del objeto


#Código principal:
persona1 = Persona("Roberto", "Correa")
print(persona1)
#print llama de forma automática a __str__

""" La palabra reservada super nos permite acceder a los métodos
    que se han sobreescrito en la clase padre (los originales)"""


