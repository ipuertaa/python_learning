#DA0 -> Data Access object
from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    #Definición de las diferentes consultas disponibles
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            #Fetchall devulve todos los registros, cada uno como una tupla
            registros = cursor.fetchall()

            #Mapeo de la clase-tabla cliente para convertir los registros a objetos tipo cliente
            clientes = []
            for registro in registros:
                #Por cada registro se crea un objeto de tipo Cliente
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])

                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        #El parámetro que se recibe es un objeto cliente
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            #Para saber cuantos registros se insertaron:
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al insertar cliente: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al actualizar cliente {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    #Insertar nuevo registro
    #cliente1 = Cliente(nombre='Alejandra', apellido='Velez', membresia=300)
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(clientes_insertados)

    #Actualizar cliente:
    #Puedo omitir el nombre de los parámetros porque los estoy enviando todos
    #cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    #clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    #print(f'Clientes actualizados: {clientes_actualizados}')

    #Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)