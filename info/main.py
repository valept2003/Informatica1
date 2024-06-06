#Victoria Pérez y Valentina Pérez Informatica 1 Trabajo final.
# Se le manda tambien carpeta con las funciones y el main debido a que presentamos problemas con github y los commits de la otra no aparecían, y tocaba mandarnos el avance por otro medio.
""" Primero se establece la conexión con MySQL y se define el cursor.
"""
from funciones import*
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="informatica1",
  password="bio123"
)

mycursor = mydb.cursor()
""" Se crea la base de datos y tablas para la gestión de información si no existen,
luego se utiliza la funcion Tablas_vacias previamente defininida para verificar que estas no poseen información
y así evitar escribir varias veces la misma información en cada tabla.
"""
mycursor.execute("CREATE DATABASE IF NOT EXISTS INFORMATICA1")
mydb.database = "INFORMATICA1"
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Ingreso (Usuario VARCHAR(255), contrasena VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Medicamentos (Lote VARCHAR(255), Nombre_medicamentos VARCHAR(255),Distribuidor INT,`Cantidad en bodega` INT, `Fecha de llegada` DATE, Precio INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Proveedores (Codigo INT, Nombre VARCHAR(255),Apellido VARCHAR(255),Documento INT,Entidad VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Ubicaciones (Codigo VARCHAR(255), Ubicacion VARCHAR(255), Telefono INT, `Entidad proveedora` VARCHAR(255))")


if Tablas_vacias("Ingreso"):
  sql_insert_users = """INSERT  INTO  Ingreso (Usuario, contrasena)  
                  VALUES (%s,%s)"""

  val_users = [
    ('Maria','123'),
    ('Felipe','123'),
    ('Jhonny','123'),
    ('Camila','123'),
    ('Kate','123')
  ]
  mycursor.executemany(sql_insert_users, val_users)
  mydb.commit()
if Tablas_vacias("Medicamentos"):
  sql_insert_meds = """INSERT  INTO  Medicamentos (Lote, Nombre_medicamentos, Distribuidor, `Cantidad en bodega`, `Fecha de llegada`, Precio)  
                  VALUES (%s,%s,%s,%s,%s,%s)"""

  val_meds = [
    ('62712','Paracetamol',11,210,'2024-02-01',8500),
    ('11234','Salbutamol',12,345,'2023-10-14',35000),
    ('98256','Amoxicilina',13,103,'2024-01-14',10000),
    ('45278','Ibuprofeno',14,225,'2024-04-01',7600),
    ('18920','Azitromicina',15,178,'2024-05-27',2500)
  ]
  mycursor.executemany(sql_insert_meds, val_meds)
  mydb.commit()
if Tablas_vacias("Ubicaciones"):
  sql_insert_ubi = """INSERT  INTO  Ubicaciones (Codigo, Ubicacion, Telefono,`Entidad proveedora`)  
                VALUES (%s,%s,%s,%s)"""

  val_ubi = [
    ('45AB3','Hospital General',59503,'Henmar'),
    ('56GH2','Hospital Alma Mater de Antioquia',56728,'Macrofarma'),
    ('89MM6','Clinica del Norte',59906,'Dermalife'),
    ('27YU6','Clinica las vegas',54432,'Suplimed'),
    ('FQ23D','Hospital la maria',50078,'Disfarmacol')
  ]
  mycursor.executemany(sql_insert_ubi, val_ubi)
  mydb.commit()

if Tablas_vacias("Proveedores"):
  sql_insert_prov = """INSERT  INTO  Proveedores (Codigo, Nombre, Apellido, Documento, Entidad)  
                  VALUES (%s,%s,%s,%s,%s)"""

  val_prov = [
    (11,'Patricio','Hernandez',1234,'Dermalife'),
    (12,'Violeta','Paez',5678,'Henmar'),
    (13,'Andres felipe','Camacho',9001,'Macrofarma'),
    (14,'Miriam','Molina',4321,'Disfarmacol'),
    (15,'Daniela Sofia','Ortega',5687,'Suplimed')
  ]
  mycursor.executemany(sql_insert_prov, val_prov)
  mydb.commit()

""" A partir de esta sección empieza el codigo que se encarga de mostrar al usuario los menus y opciones disponibles,
 validando antes que se encuentre registrado el usuario en la base de datos utilizando la función Menu_ingreso.
"""
while True:
  try:
    Menu_apertura=int(input("Ingrese opción a realizar\n1.Ingresar al sistema\n2.Salir"))
    if Menu_apertura==1:
      user=(input('Ingrese usuario')).capitalize()
      passw=input('Ingrese contraseña')
      if Menu_ingreso(user,passw):
          print('Ingresó correctamente al sistema al sistema')
          while True:
            try:
              Menu_1= int(input("Ingrese alguna opción\n1.Gestionar medicamentos\n2.Gestionar proveedores\n3.Gestionar ubicacion\n4.Salir"))
              if Menu_1==1:
                gestionar_m()
              elif Menu_1==2:
                gestionar_p()
              elif Menu_1==3:
                gestionar_u()
              elif Menu_1==4:
                    break
            except:
              print("Ingrese opción valida")
    elif Menu_apertura==2:
      break
    else:
      print("Ingrese opción valida")
  except:
    print("Intente nuevamente")