import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="informatica1",
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

def buscar_m(Lote):
    """Esta función busca el medicamento especificado por el Lote.
    Argumentos= Lote del medicamento

    """
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Medicamentos WHERE Lote=%s",(Lote,))
        medicamento=cursor.fetchone()
        print(medicamento)
    except mysql.connector.Error as error:
        print("Error:", error)

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

def ver_m():
    """Esta función muestra todos los medicamentos existentes en la base de datos

    """
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Medicamentos")
        medicamentos=cursor.fetchall()
        for medicamento in medicamentos:
            print(medicamento)
    except mysql.connector.Error as error:
        print("Error:", error)

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

def buscar_p(Codigo):
    """Esta función busca un proveedor correspondiente al codigo proporcionado.
    Argumentos= Codigo del proveedor.
    """      
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Proveedores WHERE Codigo=%s",(Codigo,))
        proveedor=cursor.fetchone()
        print(proveedor)
    except mysql.connector.Error as error:
        print("Error:", error)

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

def ver_p():
    """Esta función muestra todos los proveedores existentes en la base de datos.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Proveedores")
        proveedores=cursor.fetchall()
        for proveedor in proveedores:
            print(proveedor)
    except mysql.connector.Error as error:
        print("Error:", error)

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
def buscar_u(Codigo):
    """Esta función busca una ubicación de acuerdo al codigo proporcionado.
    Argumentos= Codigo de la ubicación.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Ubicaciones WHERE Codigo=%s",(Codigo,))
        ubicacion=cursor.fetchone()
        print(ubicacion)
    except mysql.connector.Error as error:
        print("Error:", error)
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
def ver_u():
    """Esta función muestra todas las ubicaciones existentes en la base de datos.
    """  
    cursor=mycursor
    try:
        cursor.execute("SELECT * FROM Ubicaciones")
        ubicaciones=cursor.fetchall()
        for ubicacion in ubicaciones:
            print(ubicacion)
    except mysql.connector.Error as error:
        print("Error:", error)
def codigo_proveedores():
    """Esta función imprime los proveedores disponibles mostrando sus codigos y nombres completos
    """
    sql = "SELECT Codigo, Nombre, Apellido FROM Proveedores"
    mycursor.execute(sql)
    proveedores=mycursor.fetchall()
    print("Proveedores disponibles")
    for proveedor in proveedores:
        print(f"Codigo: {proveedor[0]}, Nombre: {proveedor[1]} {proveedor[2]}")

def entidad():
    """Esta función imprime las entidades proveedoras disponibles.
    """
    sql = "SELECT Entidad FROM Proveedores"
    mycursor.execute(sql)
    entidades=mycursor.fetchall()
    print("Entidades disponibles")
    for entidad in entidades:
        print(f"Entidad: {entidad[4]}")

def Menu_m():
    """Esta función imprime un menú para la gestion de los medicamentos.
    """      
    print("1.Ingresar nuevo medicamento\n2.Actualizar información del medicamento\n3.Buscar medicamento\n4.Ver todos los medicamentos\n5.Eliminar medicamento\n6.Volver al menu principal")
def gestionar_m():
    """Esta función se encarga de gestionar la información de los medicamentos, usando funciones previamente definidas.
    """  
    while True:
        Menu_m()
        op=int(input("Ingrese opción a realizar"))
        if op==1:
            Lote=input("Ingrese Lote")
            Nombre_medicamentos=input("Ingrese nombre del medicamento")
            codigo_proveedores()
            Distribuidor=int(input("Ingrese codigo del distribuidor de la lista anterior"))
            Cantidad=int(input("Ingrese cantidad en bodega"))
            Fecha_llegada=input("Ingrese fecha de llegada (YYYY-MM-DD):")
            Precio=int(input("Ingrese precio"))
            agregar_m(Lote, Nombre_medicamentos, Distribuidor, Cantidad, Fecha_llegada, Precio)
        elif op==2:
            Lote=input("Ingrese Lote")
            Nombre_medicamentos=input("Ingrese nombre del medicamento")
            codigo_proveedores()
            Distribuidor=int(input("Ingrese codigo del distribuidor de la lista anterior"))
            Cantidad=int(input("Ingrese cantidad en bodega"))
            Fecha_llegada=input("Ingrese fecha de llegada (YYYY-MM-DD)")
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
    """Esta función imprime un menú para la gestion de los proveedores.
    """  
    print("1.Ingresar nuevo proveedor\n2.Actualizar información del proveedor\n3.Buscar proveedor\n4.Ver todos los proveedores\n5.Eliminar proveedor\n6.Volver al menu principal")
def gestionar_p():
    """Esta función se encarga de gestionar la información de los proveedores, usando funciones previamente definidas.
    """      
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
    """Esta función imprime un menu para la gestión de las ubicaciones.
    """  
    print("1.Ingresar nueva ubicación\n2.Actualizar información de la ubicación\n3.Buscar ubicación\n4.Ver todas las ubicaciones\n5.Eliminar ubicaciones\n6.Volver al menu principal")
def gestionar_u():
    """Esta función se encarga de gestionar la información de las ubicaciones, usando funciones previamente definidas.
    """  
    while True:
        Menu_u()
        op=int(input("Ingrese opción a realizar"))
        if op==1:
            Codigo=(input("Ingrese codigo de la ubicación"))
            Nombre_u=input("Ingrese nombre de la ubicación")
            Telefono=int(input("Ingrese Telefono de la ubicación"))
            entidad()
            Entidad_p=input("Ingrese entidad proveedora de la lista anterior")
            agregar_u(Codigo, Nombre_u, Telefono, Entidad_p)
        elif op==2:
            Codigo=(input("Ingrese codigo de la ubicación"))
            Nombre_u=input("Ingrese nombre de la ubicación")
            Telefono=int(input("Ingrese Telefono de la ubicación"))
            entidad()
            Entidad_p=input("Ingrese entidad proveedora de la lista anterior")
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