"""         MANEJO DE ARCHIVOS EN PYHTON

Un archivo permite almacenar información de nuestros programas,
para que cada vez que se termine de ejecutar no se pierda la
información.

    -Función open()
Es fundamental para el trabajo con archivos en pyhton

open(nombre_archivo, modo)
Los modos pueden ser:
r --> read
a --> append: para anexar sin que se pierda lo que haya antes
w --> write: para sobreescribir todo
x --> create """


#Creación de un archivo vacío
nombre_archivo = "mi_archivo.txt"

#Creación de la variable que almacena la referencia al objeto de tipo archivo
#archivo = open(nombre_archivo, 'x')
#Al ejecutarse la linea anterior, se crea un archivo de nombre: mi_archivo.txt
#El archivo no se puede crear dos veces por lo que dejo la línea comentada


#Para escribir un archivo: modo write
#Este método borra todo lo que haya antes en el archivo y sólo deja lo que se ejecuta

#Paso 1: abrir el archivo en modo escritura
#archivo = open('mi_archivo.txt', 'w')

#Paso2: con el método write, escribir en el archivo
#archivo.write('Hola mundo en el archivo\n')

#Paso3: llamar al método close
#para cerrar el buffer que se utilizó en el método open
#archivo.close()

#---

#Para leer información de un archivo: modo read

#Paso1: abrir el archivo en modo lectura
#archivo = open('mi_archivo.txt', "r")

#Paso2: usar el método read (lee todo lo que hay en el archivo)
#print(archivo.read())

#Paso3: cerrar el archivo
#archivo.close()

#---
#Para anexar información al archivo

#Paso1: abrir el archivo en modo append
#archivo = open('mi_archivo.txt', 'a')

#Paso2: escribir
#archivo.write("Anexando información")

#Paso3: cerrar el archivo
#archivo.close()

#--
#Leer varias lineas de un archivo, por default open() se abre en modo r
archivo = open('mi_archivo.txt')

#Leer todas las líneas del archivo
for linea in archivo:
    print(linea)
archivo.close()

#Obtener una lista con todo lo del archivo
archivo = open('mi_archivo.txt')
lineas = archivo.readlines()
print(lineas)
archivo.close()

#Abrir el archivo como recurso, es decir, se cierra automáticamente
with open(nombre_archivo) as archivo:
    print(archivo.read())


"""     Otros modos para trabajar archivos

- r+ --> Para lectura y escritura
- w+ --> Para lectura y escritura. Si el archivo ya existe, se sobreescribe, 
         si no existe, se crea uno nuevo
- a+ --> Lectura y agregar. Si el archivo no existe, se crea para escritura """


#Eliminar un archivo
import os
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print("Se eliminó el archivo")
else:
    print("Archivo no encontrado")


