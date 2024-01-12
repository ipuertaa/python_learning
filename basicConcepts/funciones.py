#                   FUNCIONES

""" Las funciones son bloques de código que, al invocarlas, realizan una
    acción en particular
    Para definir funciones en python:
                def nombre_funcion(parametros):
                        bloque de código
                        return (puede devolver información)

    Para llamar la función en el código: nombre_funcion(valores_parámetros)"""

print("*** Manejo de funciones ***\n")

#Definir funcion

def saludo_personal():
    nombre = input("¡Hola!, cuál es tu nombre?")
    print(f'Hola {nombre}, feliz día')


#Llamar a la función
#saludo_personal()


""" Puedo tener las funciones en otro archivo y luego invocarlas: modulos 
    Después de tener el archivo con las funciones, debo importar el archivo
    para poder utilizar la función:
                    from nombre_modulo import función"""


#           PASO DE ARGUMENTOS POR NOMBRE

def crear_persona(nombre, apellido=" ", edad=0):
    print(f'Hola {nombre} {apellido}, tienes {edad} años')


crear_persona("rosa", "martinez", 56)

""" Si no quiero enviar algún parámetro a la función, lo que puedo hacer
    es en la definición de la variable, agregar algún valor por default 
    para que cuando se ejecute la función el parámetro esté establecido"""

#Llamar a la función con argumentos por nombre
crear_persona(nombre="Ricardo", edad=30, apellido="Perez")


#           REGRESAR UNA TUPLA DE VALORES DESDE UNA FUNCIÓN
def persona_mayuscula(nombre, apellido, edad):
    print("Volviendo todo a mayúsculas...")
    return nombre.upper(), apellido.upper(), edad

#Ejecutar la función
nombre, apellido, edad = persona_mayuscula("sandra", "jimenez", 52)
print(nombre, apellido, edad)

""" Lo que hace la función es desempaquetar la tupla para asignarla a las variables
    que definimos, por la cantidad de variables debe ser igual a la cantidad de 
    elementos que returna la función """


#              ARGUMENTOS VARIABLES

#Como buena práctica de pyhton se recomienda que cuando sean argumentos variables se use *args
#También se puede enviar información en forma de diccionario **kwargs

def super_hero(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} tiene los poderes: {args} otros datos {kwargs}')


#Llamar a la función: la cantidad de superpoderes puede variar, incliso es opcional
super_hero("pepito perez", "hablar con animales", ciudad="medellin")