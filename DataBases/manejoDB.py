#           MANEJO DE BASES DE DATOS CON PYTHON

#Para conectar la base de datos con python: instalar la librería desde consola
#       -> python -m pip install mysql-connector-python

#Importar el conector de MySQL
import mysql.connector

personas_db = mysql.connector.connect(
    #Host: IP donde está instalada la base de datos, en este caso es local
    host='localhost',
    user='root',
    password='1234',
    database='personas_db'
)

#Creación del objeto tipo cursor: permite ejecutar sentencias para comunicarnos con la db
cursor = personas_db.cursor()

#Para insertar información a la base de datos
#sentencia_sql = ('INSERT INTO personas(personas, apellido, edad)''VALUES("Carlos", "Perez", 15)')

#cursor.execute(sentencia_sql)

#Para guardar de manera permanente el cambio
#personas_db.commit()

#Para actualizar un registro
#actualizar_sql = 'UPDATE personas SET personas="Victoria", apellido="Yepes", edad="25" WHERE id="7"'
#cursor.execute(actualizar_sql)
#personas_db.commit()

#Para eliminar un registro
eliminar_sql = 'DELETE FROM personas WHERE id=%s'
valor = (8,)
cursor.execute(eliminar_sql, valor)
personas_db.commit()


#Para extraer información de la base de datos
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)

#Cerrar la conexión con la base de datos
personas_db.close()
