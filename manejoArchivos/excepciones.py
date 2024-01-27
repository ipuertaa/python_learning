"""                 MANEJO DE EXCEPCIONES

Cuando ocurre un error, se pueden procesar usando:
    try: revisa si hay errores a procesar
    except: procesa el error
    else: bloque que se ejecuta cuando NO hay error
    finally: bloque que siempre se ejecuta independientemente
             si hay error o no"""

print('*** Manejo de excepciones ***')

try:
    x = int(input("Ingresa un número entero: "))
    if x == 0:
        #Para nosotros mismos arrojar una excepcion
        raise Exception('variable x = 0')

except Exception as e:
    print(f'Ocurrió un error: {e}')

else:
    print("El valor de x es diferente de cero")

finally:
    print("Valor de x verificado")