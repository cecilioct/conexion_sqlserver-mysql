import pyodbc
import pymysql


try:

   #Conexion a mysql
    conexion = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='',
                             db='alumnos')
    print("Conexión correcta con MySQL")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)


try:
    #connection = pyodbc.connect('DRIVER={SQL Server};SERVER=USKOKRUM2010;DATABASE=django_api;UID=sa;PWD=123456')
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-WIWO\SQLEXPRESS;DATABASE=alumnos;Trusted_Connection=yes;')
    print("Conexión exitosa a SQLServer.")
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Versión del servidor de SQL Server: {}".format(row))
    print("")



    #Create
      #Crear
    n =  int ( input("Cuantos registros?"))
    for x in range(n):
       Nombre = str (input("Nombre:"))
       Edad = int (input("Edad:"))
       Sueldo = int (input ("Sueldo:"))
       cursor.execute("INSERT INTO dbo.estudiantes(nombre,edad,sueldo) values (?,?,?)",Nombre,Edad,Sueldo)
       cursor.commit()

    
    #Read
    opcion = input("Consultar todos los registos Si/No:")
    if opcion != 'No':
        cursor.execute("SELECT * FROM estudiantes")
        rows = cursor.fetchall()
        for row in rows:
             print(row)
    else:
        idbusca = input ("Ingresa el Id:")
        sqlcon =("SELECT * FROM estudiantes where Id =?")
        cursor.execute(sqlcon, idbusca)
        rows = cursor.fetchall()
        for row in rows:
             print(row)
 


    #Update
    opcion = input ('Desea hacer actualizar un registro Si/No')
    if opcion != 'No':
        idbusca = int (input ("Ingresa el Id:"))
        sqlcon =("SELECT * FROM estudiantes where Id = ?")
        cursor.execute(sqlcon, idbusca)
        print("Datos actuales:")
        rows = cursor.fetchall()
        for row in rows:
             print(row)
        print("Ingrese los datos de actualizacion")
        Nombre = str (input("Nombre:"))
        Edad = int (input("Edad:"))
        Sueldo = int (input ("Sueldo:"))
        sqlcon = "UPDATE estudiantes set nombre = ?, edad = ?, sueldo = ? WHERE Id = ?"
        cursor.execute(sqlcon,(Nombre,Edad,Sueldo, idbusca))
        cursor.commit()
    #Lee de nuevo
        print("Registro actualizado")
        sqlcon =("SELECT * FROM estudiantes where Id = ?")
        cursor.execute(sqlcon, idbusca)
        rows = cursor.fetchall()
        for row in rows:
            print(row)




    #Delete
    opcion = input ('Desea hacer eliminar algun registro Si/No')
    if opcion != 'No':
         idbusca = (input ("Ingresa el Id:"))
         sqlcon ="DELETE FROM estudiantes where Id = ?"
         cursor.execute(sqlcon, idbusca)
         cursor.commit()
         print("Lista actualizada")
         cursor.execute("SELECT * FROM estudiantes")
         rows = cursor.fetchall()
         for row in rows:
             print(row)
   


except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("")
    print("La conexión ha finalizado.")