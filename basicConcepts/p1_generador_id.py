#       GENERADOR DE ID
import random

# 1. Solicitar el nombre
nombre = input("Ingrese su nombre: ")

# 2. Solicitar el apellido
apellido = input("Ingrese su apellido: ")

# 3. Solicitar fecha de nacimiento
fecha = input("Ingrese su fecha de nacimiento: ")

sub_nombre = nombre[0:2].upper()
sub_apellido = apellido[0:2].upper()
sub_fecha = fecha[2:4]

# 4. Generación del valor aleatorio de cuatro digitos. Función randon

numero = random.randint(0, 9999)


# 5. Mostrar el resultado usuando interpolación
print(f'''Hola {nombre} {apellido}
    Tu número de identificación es: {sub_nombre}{sub_apellido}{sub_fecha}{numero}
    Tu email generado por el sistema es: {nombre.lower()}.{apellido.lower()}@email.com''')
