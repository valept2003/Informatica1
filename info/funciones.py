import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="informatica 1",
  password="bio123"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS INFORMATICA1")
mydb.database = "INFORMATICA1"
mycursor = mydb.cursor()
def Menu_ingreso(user,passw):
    """Esta función se encarga de verificar la existencia del usuario y contraseña proporcionados, en la base de datos.
    Argumentos= Usuario y contraseña.
    Retorna= True si existe al menos una linea de datos que se cumpla. 
    """
    cursor=mycursor
    sql= f"SELECT * FROM Ingreso WHERE Usuario = '{user}' AND contrasena = '{passw}'"
    cursor.execute(sql)
    return cursor.fetchone()


def Menu_1():
    while True:
        op=int(input('Gestionar información de:\n1.Medicamentos\n2.Proveedores\n3.Ubicaciones\n4.Salir'))
        if op == 1:
            g_medicamentos()
        elif op == 2:
            g_proveedores()
        elif op == 3:
            g_ubicaciones()
        elif op == 4:
            print("Saliendo del sistema")
            break
        else:
            print("Opción no valida. Intente de nuevo")

def Tablas_vacias(tabla):
    """Esta función se encarga de revisar si cierta tabla está vacía, en caso de ser así retorna True.
    Argumentos= tabla
    Retorna= True si la tabla no tiene información
    """
    mycursor.execute(f"SELECT COUNT(*) FROM {tabla}")
    espacio = mycursor.fetchone()[0]
    return espacio == 0
def validar(valor):
    try:
        return(valor)
    except ValueError:
        print("Debe ingresar un número entero")
def conectar():
    return mysql.connector.connect(
  host="localhost",
  user="informatica 1",
  password="bio123"
)
#FUNCIONES CRUD PARA MEDICAMENTOS
def agregar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio):
    #Agrega un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("INSERT INTO Medicamentos (Lote, Nombre_medicamentos, Distribuidor, `Cantidad en bodega`, `Fecha de llegada`, Precio) VALUES (%s,%s,%s,%s,%s,%s)",(Lote, Nombre_medicamentos,Distribuidor, Cantidad, Fecha_llegada, Precio))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio):
    #Actualiza un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("UPDATE Medicamentos SET Nombre_medicamentos=%s, Distribuidor=%s, `Cantidad en bodega`=%s, `Fecha de llegada`=%s, Precio=%s WHERE Lote=%s",(Nombre_medicamentos, Distribuidor,Cantidad, Fecha_llegada, Precio, Lote))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_m(Lote):
    #Busca un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Medicamentos WHERE Lote=%s",(Lote,))
        medicamento=cursor.fetchone()
        return medicamento
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def eliminar_m(Lote):
    #Elimina un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("DELETE FROM Medicamentos WHERE Lote=%s", (Lote,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_m():
    #Muestra la informacion de los medicamentos almacenados
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Medicamentos")
        medicamentos=cursor.fetchall()
        return medicamentos
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
#FUNCIONES DE CRUD PARA PROVEEDORES
def agregar_p(Codigo, Nombre, Apellido, Documento, Entidad):
    cursor=mydb.cursor()
    try:
        cursor.execute("INSERT INTO Proveedores (Codigo, Nombre, Apellido, Documento, Entidad) VALUES (%s,%s,%s,%s,%s)",(Codigo, Nombre, Apellido, Documento, Entidad))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_p(Codigo, Nombre, Apellido, Documento, Entidad):
    cursor=mydb.cursor()
    try:
        cursor.execute("UPDATE Proveedores SET Nombre=%s, Apellido=%s, Documento=%s, Entidad=%s WHERE Codigo=%s",(Nombre, Apellido, Documento, Entidad, Codigo))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_m(Codigo):
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Proveedores WHERE Codigo=%s",(Codigo,))
        proveedor=cursor.fetchone()
        return proveedor
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def eliminar_m(Codigo):
    cursor=mydb.cursor()
    try:
        cursor.execute("DELETE FROM Proveedores WHERE Codigo=%s", (Codigo,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_m():
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Proveedores")
        proveedores=cursor.fetchall()
        return proveedores
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
#FUNCIONES CRUD PARA UBICACIONES
def agregar_u(Codigo, Nombre_u, Telefono, Entidad_p):
    #Agrega un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("INSERT INTO Ubicaciones (Codigo, Ubicacion, Telefono, `Entidad proveedora`) VALUES (%s,%s,%s,%s)",(Codigo, Nombre_u, Telefono, Entidad_p))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_u(Codigo, Nombre_u, Telefono, Entidad_p):
    #Actualiza un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("UPDATE Ubicaciones SET Ubicacion=%s, Telefono=%s, `Entidad proveedora`=%s WHERE Codigo=%s",(Nombre_u, Telefono, Entidad_p, Codigo))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_u(Codigo):
    #Busca un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Ubicaciones WHERE Codigo=%s",(Codigo,))
        ubicacion=cursor.fetchone()
        return ubicacion
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def eliminar_m(Codigo):
    #Elimina un medicamento
    cursor=mydb.cursor()
    try:
        cursor.execute("DELETE FROM Ubicaciones WHERE Codigo=%s", (Codigo,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_u():
    #Muestra la informacion de los medicamentos almacenados
    cursor=mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Ubicaciones")
        ubicaciones=cursor.fetchall()
        return ubicaciones
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()