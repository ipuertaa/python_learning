#               ATRIBUTOS DE CLASE

""" Los atributos que he trabajdo anteriormente se asocian a los objetos,
    cuando se crean distintos objetos de esa clase, cada atributo
    de instancia tendrá su propio valor (no afecta a los demás)
            --> Los atributos de instancia u objeto son variables locales
                de cadda objeto
                Los identifico porque usan self
    Un atributo de clase se asocia directamente a la clase, de modo que
    si se crean diferentes objetos el atributo es compartido en todas las
    instancias
            --> Los atributos de clase son variables globales a todos los
                objetos, si se caambia, cambiará a en todos los objetos
                Se trabajan dentro de la clase pero fuera de los métodos"""


class Persona:
    atributo_clase = 0

    def __init__(self):
        self.atributo_instancia = 0


print("*** Atributos de clase ***")

#Para acceder al atributo de clase no es necesario crear un objeto
print(f'El atirbuto de clase es: {Persona.atributo_clase}')
#Modificar el atributo de clase (común a todos los objetos de la clase)
Persona.atributo_clase = 10
print(f'Atributo modificado: {Persona.atributo_clase}')

#Creación de un objeto de esa clase
persona1 = Persona()
persona1.atributo_instancia = 20

#Creación de un segundo objeto
persona2 = Persona()
persona2.atributo_instancia = 30

""" Error que cometí: tratar de modificar el atributo de clase desde
    la instancia: aquí lo que estaba haciendo era crear un nuevo
    atributo de instancia asociado únicamente a persona2, por lo tanto
    en el otro objeto no se veía reflejado el cambio"""
#persona2.atributo_clase = 1000

""" Corrección: si se desea modificar el atributo de clase para todas 
    las instancia de una clase, se debe hacer a través del nombre de 
    la clase, no a través de las instancias"""
Persona.atributo_clase = 1000

print(f'''El atributo de instancia de 1 es: {persona1.atributo_instancia}
El atributo de instancia de 2 es: {persona2.atributo_instancia}
El atributo de clase desde la persona1: {persona1.atributo_clase}
El atributo de clase desde persona2 es: {persona2.atributo_clase}''')


#           EJEMPLO DE ATRIBUTO DE CLASES

class ContPersonas:
    #Atributos de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        ContPersonas.contador_personas += 1
        self.id = ContPersonas.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def asignar_id(self):
        print(f'Id: {self.id} - {self.nombre} {self.apellido}')
        return id


#Creación de las personas
persona_id1 = ContPersonas("Sofia", "Jimenez")
persona_id2 = ContPersonas("Ramiro", "Meneses")
persona_id3 = ContPersonas("Don", "Omar")
persona_id1.asignar_id()
persona_id2.asignar_id()
persona_id3.asignar_id()