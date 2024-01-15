#           INTRODUCCIÓN A VARIABLES
# Los archivos .py también se llaman "scripts"

#Variable tipo int - entero
entero = 10

#Variable tipo float - decimal
flotante = 5.7

#Variable tipo string (str) - texto
string = 'Hola'
#Se usa comilla simple o doble

#       REGLAS PARA DEFINIR EL NOMBRE DE LAS VARIABLES

# Comenzar con una letra o _. Puede continuar con letras, números o _
# Sensible a mayúsculas y minúsculas
# No se pueden usar palabras reservadas =  class, if, for, while...
# Buena práctica: separar palabras con _ (snake case)


#       STRINGS

#Para agregar saltos de linea \n
nombre = 'Isabel \nPuerta'
#print(nombre)

#Para agregar un tabulador \t
nombre_tab = '\tIsabel\tPuerta'
#print(nombre)


#       SUBCADENAS
mensaje = 'Hola mundo'

#Si quiero recuperar partes del mensaje, fijarme en los índices (pilas que el final no se incluye)
# subcadena = cadena[indice_inicio:indice_final + 1]
sub_mensaje = mensaje[0:4]
#Submensaje es una nueva cadena diferente a la inicial
#print(sub_mensaje)

#       METODOS DE CADENAS (string.metodo. Los métodos son las funciones que operan sobre strings)

#Si quiero convertir a mayúsculas
msg_mayusculas = mensaje.upper()
#print(msg_mayusculas)

#Si quiero convertir a minúsculas
msg_minusculas = mensaje.lower()
#print(msg_minusculas)


#       FORMAS DE DAR FORMATO A STRINGS

#Para imprimir varios valores print(str1 , str2 , ...)

#Concatenación: unir dos o más strings --> +
variable_hola = 'Hola'
variable_mundo = 'Mundo'
variable_total = variable_hola + ' ' + variable_mundo
#print(variable_total)

#Interpolación de cadenas, usando la letra f
mensaje_nuevo = f'Mi string: {variable_hola} {variable_mundo}'
#print(mensaje_nuevo)

#Interpolación con multi-lineas f''' esta opción respeta los espacios que pongo
print(f'''Mi String: 
    {variable_hola} 
        {variable_mundo}''')