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
def Tablas_vacias(tabla):
    """Esta función se encarga de revisar si cierta tabla está vacía, en caso de ser así retorna True.
    Argumentos= tabla
    Retorna= True si la tabla no tiene información
    """
    mycursor.execute(f"SELECT COUNT(*) FROM {tabla}")
    espacio = mycursor.fetchone()[0]
    return espacio == 0
def agregar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio):
    """Esta función agrega un medicamento con la información que se le entregue.
    Argumentos= Datos del medicamento
    """    
    cursor=mycursor
    try:
        cursor.execute("INSERT INTO Medicamentos (Lote, Nombre_medicamentos, Distribuidor, `Cantidad en bodega`, `Fecha de llegada`, Precio) VALUES (%s,%s,%s,%s,%s,%s)",(Lote, Nombre_medicamentos,Distribuidor, Cantidad, Fecha_llegada, Precio))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio):
    """Esta función actualiza la información de un medicamentos a partir de su Lote.
    Argumentos= Nueva información
    """
    cursor=mycursor
    try:
        cursor.execute("UPDATE Medicamentos SET Nombre_medicamentos=%s, Distribuidor=%s, `Cantidad en bodega`=%s, `Fecha de llegada`=%s, Precio=%s WHERE Lote=%s",(Nombre_medicamentos, Distribuidor,Cantidad, Fecha_llegada, Precio, Lote))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_m(Lote):
    """Esta función busca el medicamento especificado por el Lote.
    Argumentos= Lote del medicamento
    Retorna: El medicamento si encuentra alguna coincidencia,si no retorna None
    """
    cursor=mycursor
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
    """Esta función elimina el medicamento especificado por el Lote.
    Argumentos= Lote del medicamento
    """
    cursor=mycursor
    try:
        cursor.execute("DELETE FROM Medicamentos WHERE Lote=%s", (Lote,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_m():
    """Esta función muestra todos los medicamentos existentes en la base de datos
    Retorna: Una lista con todos los medicamentos si encuentra alguno, sino una lista vacía.
    """
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Medicamentos")
        medicamentos=cursor.fetchall()
        return medicamentos
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def agregar_p(Codigo, Nombre, Apellido, Documento, Entidad):
    """Esta función agrega un proveedor con la información que se le entregue.
    Argumentos= Datos del proveedor
    """  
    cursor=mycursor
    try:
        cursor.execute("INSERT INTO Proveedores (Codigo, Nombre, Apellido, Documento, Entidad) VALUES (%s,%s,%s,%s,%s)",(Codigo, Nombre, Apellido, Documento, Entidad))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_p(Codigo, Nombre, Apellido, Documento, Entidad):
    """Esta función actualiza la información de un proveedor correspondiente al codigo proporcionado.
    Argumentos= Datos a actualizar del proveedor.
    """  
    cursor=mycursor
    try:
        cursor.execute("UPDATE Proveedores SET Nombre=%s, Apellido=%s, Documento=%s, Entidad=%s WHERE Codigo=%s",(Nombre, Apellido, Documento, Entidad, Codigo))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_p(Codigo):
    """Esta función busca un proveedor correspondiente al codigo proporcionado.
    Argumentos= Codigo del proveedor.
    Retorna: Tupla con el proveedor encontrado.
    """      
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Proveedores WHERE Codigo=%s",(Codigo,))
        proveedor=cursor.fetchone()
        return proveedor
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def eliminar_p(Codigo):
    """Esta función elimina a un proveedor correspondiente al codigo proporcionado.
    Argumentos= Codigo del proveedor.
    """  
    cursor=mycursor
    try:
        cursor.execute("DELETE FROM Proveedores WHERE Codigo=%s", (Codigo,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_p():
    """Esta función muestra todos los proveedores existentes en la base de datos.
    Retorna: Lista de tuplas con todos los proveedores, sino una lista vacía.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Proveedores")
        proveedores=cursor.fetchall()
        return proveedores
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()

def agregar_u(Codigo, Nombre_u, Telefono, Entidad_p):
    """Esta función agrega una nueva ubicación con la información proporcionada.
    Argumentos= Datos de la nueva ubicación
    """  
    cursor=mycursor
    try:
        cursor.execute("INSERT INTO Ubicaciones (Codigo, Ubicacion, Telefono, `Entidad proveedora`) VALUES (%s,%s,%s,%s)",(Codigo, Nombre_u, Telefono, Entidad_p))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def actualizar_u(Codigo, Nombre_u, Telefono, Entidad_p):
    """Esta función actualiza la información de una ubicación correspondiente al codigo proporcionado
    Argumentos= Datos nuevos de la ubicación.
    """  
    cursor=mycursor
    try:
        cursor.execute("UPDATE Ubicaciones SET Ubicacion=%s, Telefono=%s, `Entidad proveedora`=%s WHERE Codigo=%s",(Nombre_u, Telefono, Entidad_p, Codigo))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def buscar_u(Codigo):
    """Esta función busca una ubicación de acuerdo al codigo proporcionado.
    Argumentos= Codigo de la ubicación.
    Retorna: Tupla con la ubicación encontrada.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Ubicaciones WHERE Codigo=%s",(Codigo,))
        ubicacion=cursor.fetchone()
        return ubicacion
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def eliminar_u(Codigo):
    """Esta función elimina una ubicación correpondiente al codigo proporcionado.
    Argumentos= Codigo de la ubicación.
    """  
    cursor=mycursor
    try:
        cursor.execute("DELETE FROM Ubicaciones WHERE Codigo=%s", (Codigo,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def ver_u():
    """Esta función muestra todas las ubicaciones existentes en la base de datos.
    Retorna: Lista de tuplas con las ubicaciones encontradas, sino una lista vacia.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Ubicaciones")
        ubicaciones=cursor.fetchall()
        return ubicaciones
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        mydb.close()
def Menu_m():
    print("1.Ingresar nuevo medicamento\n2.Actualizar información del medicamento\n3.Buscar medicamento\n4.Ver todos los medicamentos\n5.Eliminar medicamento\n6.Volver al menu principal")
def gestionar_m():
    while True:
        Menu_m()
        op=int(input("Ingrese opción a realizar"))
        if op==1:
            Lote=input("Ingrese Lote")
            Nombre_medicamentos=input("Ingrese nombre del medicamento")
            Distribuidor=int(input("Ingrese codigo del distribuidor"))
            Cantidad=int(input("Ingrese cantidad en bodega"))
            Fecha_llegada=input("Ingrese fecha de llegada")
            Precio=int(input("Ingrese precio"))
            agregar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio)
        elif op==2:
            Lote=input("Ingrese Lote")
            Nombre_medicamentos=input("Ingrese nombre del medicamento")
            Distribuidor=int(input("Ingrese codigo del distribuidor"))
            Cantidad=int(input("Ingrese cantidad en bodega"))
            Fecha_llegada=input("Ingrese fecha de llegada")
            Precio=int(input("Ingrese precio"))
            actualizar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio)
        elif op==3:
            Lote=input("Ingrese Lote")
            buscar_m(Lote)
        elif op==4:
            ver_m()
        elif op==5:
            Lote=input("Ingrese Lote")
            eliminar_m(Lote)
        elif op==6:
            break
        else:
            print("Ingrese opción valida")
def Menu_p():
    print("1.Ingresar nuevo proveedor\n2.Actualizar información del proveedor\n3.Buscar proveedor\n4.Ver todos los proveedores\n5.Eliminar proveedor\n6.Volver al menu principal")
def gestionar_p():
    while True:
        Menu_p()
        op=int(input("Ingrese opción a realizar"))
        if op==1:
            Codigo=int(input("Ingrese codigo del proveedor"))
            Nombre=input("Ingrese nombre del proveedor")
            Apellido=input("Ingrese apellido del proveedor")
            Documento=int(input("Ingrese documento del proveedor"))
            Entidad=input("Ingrese entidad del proveedor")
            agregar_p(Codigo, Nombre, Apellido, Documento, Entidad)
        elif op==2:
            Codigo=int(input("Ingrese nuevo codigo del proveedor"))
            Nombre=input("Ingrese nuevo nombre del proveedor")
            Apellido=input("Ingrese nuevo apellido del proveedor")
            Documento=int(input("Ingrese nuevo documento del proveedor"))
            Entidad=input("Ingrese nueva entidad del proveedor")
            actualizar_p(Codigo, Nombre, Apellido, Documento, Entidad)
        elif op==3:
            Codigo=int(input("Ingrese codigo del proveedor"))
            buscar_p(Codigo)
        elif op==4:
            ver_p()
        elif op==5:
            Codigo=int(input("Ingrese codigo del proveedor"))
            eliminar_p(Codigo)
        elif op==6:
            break
        else:
            print("Ingrese opción valida")
def Menu_u():
    print("1.Ingresar nueva ubicación\n2.Actualizar información de la ubicación\n3.Buscar ubicación\n4.Ver todas las ubicaciones\n5.Eliminar ubicaciones\n6.Volver al menu principal")
def gestionar_u():
    while True:
        Menu_u()
        op=int(input("Ingrese opción a realizar"))
        if op==1:
            Codigo=(input("Ingrese codigo de la ubicación"))
            Nombre_u=input("Ingrese nombre de la ubicación")
            Telefono=int(input("Ingrese Telefono de la ubicación"))
            Entidad_p=input("Ingrese entidad proveedora")
            agregar_u(Codigo, Nombre_u, Telefono, Entidad_p)
        elif op==2:
            Codigo=(input("Ingrese codigo de la ubicación"))
            Nombre_u=input("Ingrese nombre de la ubicación")
            Telefono=int(input("Ingrese Telefono de la ubicación"))
            Entidad_p=input("Ingrese entidad proveedora")
            actualizar_u(Codigo, Nombre_u, Telefono, Entidad_p)
        elif op==3:
            Codigo=(input("Ingrese codigo de la ubicación"))
            buscar_u(Codigo)
        elif op==4:
            ver_u()
        elif op==5:
            Codigo=(input("Ingrese codigo de la ubicación"))
            eliminar_u(Codigo)
        elif op==6:
            break
        else:
            print("Ingrese opción valida")