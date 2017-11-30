#Author: juana gutierrez
#Group: GITI9072-e
import psycopg2

#This function do the connection into Python and postrgeSQL
def crear_tablas():
    # The script create the Table 'Registros' in the Database 'base1'
    comandos = ("CREATE TABLE calculos("
                "id SERIAL PRIMARY KEY,"
                "total VARCHAR NOT NULL)")

    conexion = None
    #Here we are going the insert the params for the connection with postgreSQL
    try:
        configuracionDB = {'host': '127.0.0.1',
                           'port': '5433',
                           'user': 'postgres',
                           'password': '1234',
                           'database': 'test',}
        conexion = psycopg2.connect(**configuracionDB)
        #Here we create the cursor for execute the commands of the Database
        cursor = conexion.cursor()
        cursor.execute(comandos)
        #Here we close the cursor
        cursor.close()
        conexion.commit()
    #Here is created the error of the Database if the params are not good
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    #Here we close the connection with the Database
    finally:
        if conexion is not None:
            conexion.close()


if __name__ == '__main__':
    crear_tablas()

