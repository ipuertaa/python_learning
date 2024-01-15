#       CONSTRUCTORES EN PYTHON

#El paso de crear el objeto y luego asignarle atributos puede simplificarse

class Persona:
    #En lugar de una función de inicialización, se usa el constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Su nombre es: {self.nombre} {self.apellido}')


#Código princial
persona1 = Persona("Karla", "Perez")
#Podemos ver que se instanció el objeto y directamente se agregaron sus atributos
persona1.mostrar_persona()
#Podemos acceder a los atributos
persona1.nombre = "Marcos"
persona1.mostrar_persona()

""" En este momento desde la variable de persona1 se podrían cambiar los atributos del 
    objeto, esto se conoce como sin encapsulamiento o atributos públicos
    No es muy recomendado que se acceda a los atributos directamente sino que se haga 
    meediante métodos
    
    Para encapsular o proteger los atributos se puede:
        1. Agregar un _al principio en la definición del atributo (igual se podría 
           acceder sólo poniendo el _ pero eso no es buena práctica de programación)
        2. Agregar __ al principio de la definición del atributo --> atributo privado
           en este caso no se puede acceder al atributo (es más estricto que el caso anterior)
        
        Nota: igual yo podria poner persona1.nombre = julanito así el atributo esté 
        protegido pero eso va a crear ese atirbuto en un lugar diferente de la memoria y 
        no sería reconocible por los otros objetos --> atributo al vuelo
        """

# Creación de la clase con atributos protegidos


class PersonaProtegida:
    def __init__(self, nombre, apellido):
        self.__nombreP = nombre      #Atributo protegido
        self.__apellidoP = apellido  #Atributo privado

    #Después del constructor de la clase van los métodos get y set
    def get_nombre(self):
        return self.__nombreP

    def set_nombre(self, nombre):
        self.__nombreP = nombre

    def get_apellido(self):
        return self.__apellidoP

    def set_apellido(self, apellido):
        self.__apellidoP = apellido

    def mostrar_nombre(self):
        print(f'Su nombre es: {self.__nombreP} {self.__apellidoP}')


persona_p = PersonaProtegida("Karla", "Protegida")
persona_p.mostrar_nombre()

#Cambiando los atributos usando los nuevos métodos
persona_p.set_nombre("Maria")
persona_p.set_apellido("Medrano")
print(persona_p.get_nombre(), persona_p.get_apellido())
persona_p.mostrar_nombre()