from dal.db import Db
import hashlib
def poblar_tablas():
    #tabla roles
    datos_roles = [(1,'administrador'),(2,'usuario'),(3,'vendedor')]
    consulta_roles = '''INSERT INTO "Roles" VALUES (?,?)'''
    cant_filas_roles = int((Db.consulta_db(f'SELECT COUNT(*) FROM "Roles" ',True))[0])

    consulta_cat_prod = '''INSERT INTO "Categorias_productos" VALUES (?,?)'''
    datos_cat_prod = [
    (1,'bebidas'),
    (2,'comestibles'),
    (3,'articulos de limpieza'),
    (4,'higiene personal'),
    (5,'bazar'),
    (6,'alimento para mascotas')]
    cant_filas_categ_prod =  int(Db.consulta_db(f'SELECT COUNT(*) FROM "Categorias_productos" ',True)[0])

    lista_datos = [['Roles',consulta_roles,datos_roles,cant_filas_roles],['Categorias_productos',consulta_cat_prod,datos_cat_prod,cant_filas_categ_prod]]

    for dato in lista_datos:
        if(dato[3] == 0):
            print(f'Poblando tabla {dato[0]}')
            Db.modifica_db_varios(dato[1],dato[2])


def crear_tablas(): #tablas para guardar los datos de los usuarios
    tabla_cat_prod = '''CREATE TABLE IF NOT EXISTS "Categorias_productos"
                        (
	                        "codigo"	INTEGER,
	                        "categoria"	TEXT,
	                        PRIMARY KEY("codigo")
                        );'''
    tabla_productos = '''CREATE TABLE IF NOT EXISTS "Productos"
                      (
                        "codigo"	INTEGER,
                        "id"	TEXT NOT NULL,
                        "marca"	TEXT NOT NULL,
                        "stock"	INTEGER NOT NULL,
                        "precio"	REAL NOT NULL,
                        "categoria"	INTEGER,
                        FOREIGN KEY("categoria") REFERENCES "Categorias_productos"("codigo"),
                        PRIMARY KEY("codigo" AUTOINCREMENT)
                        );'''
    tabla_pedidos = '''CREATE TABLE IF NOT EXISTS "Pedidos" (
	                "codigo"	INTEGER,
	                "fecha"	TEXT,
	                "usuario"	TEXT,
	                "monto_total"	REAL,
	                PRIMARY KEY("codigo" AUTOINCREMENT)
                    );'''
    tabla_detalle_pedidos = '''CREATE TABLE IF NOT EXISTS "Detalle_pedidos" (
                            "producto"	TEXT,"precio_unitario"	REAL,
                            "id"	INTEGER,"codigo_pedido"	INTEGER,
                            PRIMARY KEY("id" AUTOINCREMENT),
                            FOREIGN KEY("codigo_pedido") REFERENCES "Pedidos"("codigo")
                            );'''
    tabla_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                    "id"	INTEGER,"tipo"	TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
                    );'''
    tabla_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                        "id"	TEXT UNIQUE,"password"	TEXT NOT NULL,
                        "nombre" TEXT, "apellido" TEXT,
                        "dni" INTEGER,"email"	TEXT NOT NULL,
                        "domicilio"	TEXT NOT NULL,
                        "ciudad" TEXT NOT NULL,
                        "telefono"	INTEGER,
                        "activo"	INTEGER,"tipo"	INTEGER,
                        FOREIGN KEY("tipo") REFERENCES "Roles"("id"),
                        PRIMARY KEY("id")
                        );'''

    dict_consultas = {
                        "categoria_productos":tabla_cat_prod ,
                        "productos":tabla_productos,
                        "roles_usuarios":tabla_roles,
                        "usuarios":tabla_usuarios,
                        "pedidos":tabla_pedidos,
                        "detalles_pedidos":tabla_detalle_pedidos
                     }
    for nomb_tabla,consulta in dict_consultas.items():
        print(f"Creando tablas para {nomb_tabla}")
        Db.modifica_db(consulta)

def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()

#recibe el nombre de usuario y password de la gui // este modulo va en bll
def validar_usuario(usuario,password):#requiere como parametros los datos que recibe de la GUI
    consulta = '''SELECT "tipo" FROM 'Usuarios'
                                 WHERE id = ?
                                AND password = ?
                                AND activo = 1'''
    #encriptar contasenia antes de llamar a la validacion
    password = encriptar_contraseña(password)
    entrada = (usuario,password)
    return Db.busca_uno_varios(consulta,entrada)

def existe_usuario(user):
    consulta = "SELECT 'id' FROM 'Usuarios' WHERE id = ?"
    parametro = (user,)
    return Db.busca_uno_varios(consulta,parametro)

def password_iguales(contrasenia,confirmacion):
    if(contrasenia == confirmacion):
        return True
    else:
        return False

def agregar_usuario(usuario,password,nombre,apellido,dni,email,direccion,ciudad,telefono,rolId):
    sql = "INSERT INTO Usuarios VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    password = encriptar_contraseña(password)
    argumento=(usuario,password,nombre,apellido,dni,email,direccion,ciudad,telefono,1,rolId)
    Db.modifica_db(sql,argumento)

def es_text_sin_espacios(variable):
    no_tiene_espacio = True
    for c in variable:
        if c == ' ':
            no_tiene_espacio = False
    return (variable.isprintable() and no_tiene_espacio)
def es_text_con_espacios(variable):
    return (variable.isprintable() and (not variable.isdigit()) )
def es_numero(numero):
    return numero.isdigit()

def valida_nombre_ape(var):
    tiene_espacio = False
    for c in var:
        if c == ' ':
            tiene_espacio = True
    return (var.isalpha() or tiene_espacio)
def valida_domicilio(domicilio):
    tiene_espacio = False
    for c in domicilio:
        if c == ' ':
            tiene_espacio = True
    return (domicilio.isalnum() or tiene_espacio)
def valida_ciudad(ciudad):
    tiene_espacio = False
    for c in ciudad:
        if c == ' ':
            tiene_espacio = True
    return ciudad.isalpha() or tiene_espacio
def valida_email(email):
    cntiene_arroba = False
    cntiene_pnto = False
    no_tiene_espacio = True
    for c in email:
        if c == '@':
            cntiene_arroba = True
        if c =='.':
            cntiene_pnto = True
        if c == ' ':
            no_tiene_espacio = False
    return (email.isprintable() and (not email.isdigit()) and cntiene_arroba and cntiene_pnto and no_tiene_espacio)



def valida_datos_registro(usuario,contrasenia,confirmacion,nombre,apellido,dni,email,domicilio,ciudad,telefono):
    return (es_text_sin_espacios(usuario)and (not es_numero(usuario)) and (not(existe_usuario(usuario)))and password_iguales(contrasenia,confirmacion)and
     es_text_sin_espacios(contrasenia) and  valida_nombre_ape(nombre)and valida_nombre_ape(apellido)and es_numero(dni) and
      valida_domicilio(domicilio)and valida_ciudad(ciudad)and es_numero(telefono) and valida_email(email))

def usuario_administrador(usuario):
    sql = 'SELECT "tipo" FROM "Usuarios" WHERE id = ?'
    parametro = (usuario,)
    resp = Db.consulta_db(sql,True,parametro)
    resp = int(resp[0])
    if resp == 1:
        return True
    else:
        return False