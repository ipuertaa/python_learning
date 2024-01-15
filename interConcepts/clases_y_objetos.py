#                   CLASES Y OBJETOS

""" Python es un lenguaje de programación orientado a objetos

    Objeto: representación de una entidad de la vida real en el programa
    Para crear un objeto se debe crear una clase o plantilla

    Clase: representa las carácterísticas del los objetos
    Es como el plano de un tornillo --> a partir de un sólo plano con
    las carácterísticas del tornillo puedo fabricar muchos de ellos
    (este proceso de fabricación se llama "instanciar la clase")

    Una clase tiene atributos (características) y métodos (acciones que puede
    realizar el objeto) """


#Clase para una agenda de contactos
class Contacto:
    #Definición de un método (función dentro de una clase)
    def init_contacto(self, nombre, apellido, celular, email):
        """ Por default, el primer parámetro que se asigna es self
            Los otros parámetros luego vendrán siendo nuestros atributos.
            Los nombres de los parámetros y los atributos podrían ser diferentes
            pero por buenas prácticas se recomienda que sean iguales
            Para aregrar los atributos a la clase se usa self
            Para acceder a los atributos de una clase se usa self"""
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_contacto(self):
        print(f'''Contacto
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Celular: {self.celular}
            Email: {self.email}
            Dirección de memoria: {hex(id(self))}''')


""" Ya se definió la clase Contacto. Posteriormente, con esa clase se podrán crear
    diferntes objetos, es decir diferentes contactos, cada uno con atributos 
    diferentes (Por ejemplo Sofia Perez y Carlos Franco, etc)
    
    El método init_contacto va a crear el objeto en memoria y a inicializar los valores
    de los atributos
    
    Recordar que los objetos son instancias de la clase
    
    Self es una variable que apunta a los objetos que se está ejecutando en un momento dado"""


#Código principal:

print("*** Clases y objetos en pyhton ***")

#Creación del primer objeto: en este momento se crea un objeto vacío.
#la variable con contacto1 apunta a un objeto de tipo Contacto
contacto1 = Contacto()
#Acceder a los atributos del objeto creado: self se pasa de manera automática
contacto1.init_contacto("Layla", "Acosta", "12524", "layla@email.com")

contacto1.mostrar_contacto()

#Creación del segundo objeto:
contacto2 = Contacto()
contacto2.init_contacto("Carlos", "Gomez", "14553", "cgomez@email.com")
contacto2.mostrar_contacto()


""" Todos los tipos de datos en pyhton corresponde a objetos, por ejemplo, al crear una variable 
    numero = 10, no quiere decir que se almacene literalmente 10, sino que numero es una variable
    que apunta a un objeto de tipo entero con el atributo de 10. La variable como tal solo almacena 
    la dirección de memoria donde está ese objeto --> verificar usando el comando id 
    Si quiero saber el tipo de la clase, usar el comando type
    Por ejemplo una lista es un objeto tipo list que hace es almacenar la dirección de memoria 
    donde se crearon los diferentes objetos (recordar que pueden ser de diferentes tipos)
    
    En conclusión: int, str, list... son clases, que tienen atributos y métodos asociados, al crear
    variables de ese tipo lo que estamos haciendo es instanciar esas clases"""

""" En python hay una memoria donde se almacenan las variables y otra donde se almacenan los objetos
    Ejemlplo: numero(variable que apunta al objeto) --> Memoria stack. Es una memoria que va apilando
              10(objeto tipo entero) --> Memoria heap. Los objetos permanecen ahí siempre que haya una 
                                                        apuntando a ellos. Pyhton es el que los elimina"""
