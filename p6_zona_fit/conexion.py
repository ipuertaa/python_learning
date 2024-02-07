from mysql.connector import pooling
from mysql.connector import Error


class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = '1234'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        # Se crea el objeto pool si no existe
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                #print(f'Nombre del pool: {cls.pool.pool_name}')
                #print(f'Tamaño del pool: {cls.pool.pool_size}')
                return cls.pool

            except Error as e:
                print(f'Ocurrió un error al obtener el pool: {e}')

        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


#Para ejecutar pruebas desde un archivo particular
if __name__ == '__main__':
    #Obteniendo un objeto conexión
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)

    #Liberando un objeto conexion
    Conexion.liberar_conexion(cnx1)