#       ENTRADA DE DATOS POR CONSOLA

#mensaje = input('Proporciona un mensaje: ')

#Usando interpolación de cadenas
#print(f'El mensaje recibido es: {mensaje}')

numero1 = int(input('Ingrese un primer número: '))
numero2 = int(input('Ingrese un segundo número: '))
suma = numero1 + numero2
print(f'''El primer número es: {numero1}
El segundo número es: {numero2}
La suma es: {suma}''')

#Para que la suma no sean dos cadenas juntas se debe covertir el tipo de entrada
#Strign a formato numérico. La función input(recibe strings)
#Para eso se usa la función int() que convierte cadena a tipo entero
#Si son decimales, se usa la función float()