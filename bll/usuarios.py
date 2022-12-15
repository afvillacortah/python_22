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
                        "es_activo" INTEGER DEFAULT 1,
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
                            "id"	INTEGER,
                            "producto"	TEXT,"cantidad"	INTEGER,
                            "codigo_pedido"	INTEGER,
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
                        "activo"	INTEGER DEFAULT 1,"tipo"	INTEGER,
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
def listar_productos(nombre):
    sql = f"""SELECT p.codigo,p.id,p.marca,p.stock,p.precio,p.categoria,c.categoria categoria
     FROM Productos p 
     INNER JOIN Categorias_productos c ON p.categoria = c.codigo
     WHERE  p.stock > 0 AND p.es_activo = 1 AND (p.id LIKE '%{nombre.lower()}%' OR p.id LIKE '%{nombre.capitalize()}%') 
    ;"""
    resultado = Db.consulta_db(sql)
    return resultado

def obtener_datos_prod(cod_prod,cant_elegida):
    sql = f"""SELECT p.codigo,p.id,p.marca,p.precio,p.categoria,c.categoria categoria
     FROM Productos p 
     INNER JOIN Categorias_productos c ON p.categoria = c.codigo
     WHERE p.codigo = '{cod_prod}' AND p.stock >= '{cant_elegida}' AND p.es_activo = 1 ;""" 
    resultado = Db.consulta_db(sql,True) 
    
    return resultado

def retorna_stock_disponible(codigo):
    sql =f'SELECT stock from Productos WHERE codigo= {codigo}'
    stock_disponible = Db.consulta_db(sql,True)
    stock_disponible = stock_disponible[0]
    return stock_disponible

def comprar_producto(codigo,cantidad):
    sql = f"""UPDATE Productos SET stock = stock -'{cantidad}'
             WHERE codigo = '{codigo}' """ 
    Db.modifica_db(sql)

def valida_lista_productos(lista_compra):
    for item in lista_compra:   #valida stock y si pasa la validacion compra el producto
        if(retorna_stock_disponible(item[0]) >= item[3]):
            comprar_producto(item[0],item[3])
            print(f'Compro: {item[3]}  Unidades de : {item[1]} !')
        else:
            lista_compra.remove(item)#quitar de la lista de compra


def obtener_codigo_compra():
    sql ="SELECT MAX(codigo)FROM 'Pedidos' "
    resp = Db.consulta_db(sql,True)
    if(resp[0] == None):
        resp = 1
        return(resp)
    else:
        resp = int(resp[0]) + 1
        return(resp) 

def obtener_codigo_inicial_detalle_pedidos():
    sql ="SELECT MAX(id) FROM 'Detalle_pedidos' "
    resp = Db.consulta_db(sql,True)
    if(resp[0] == None):
        resp = 1
        return(resp)
    else:
        resp = int(resp[0]) + 1
        return(resp) 

def agregar_detalle_compra(id,nombre,cantidad,cod):
    sql ="INSERT INTO Detalle_pedidos VALUES (?,?,?,?)"
    argumento =(id,nombre,cantidad,cod)
    Db.modifica_db(sql,argumento)

def retorna_fecha():
    fecha = Db.consulta_db('SELECT date();',True)
    fecha=fecha[0]
    return fecha

def registrar_compra(lista_compra,usuario):
    codigo_pedido = obtener_codigo_compra()
    id_detalle_pedido =obtener_codigo_inicial_detalle_pedidos()
    total_compra = 0
    for art in lista_compra:
        agregar_detalle_compra(id_detalle_pedido,art[1]+" "+art[2],art[3],codigo_pedido)
        id_detalle_pedido += 1
        total_compra += art[4]
    fecha = retorna_fecha()
    #agregar compra
    sql = "INSERT INTO Pedidos VALUES (?,?,?,?)"
    argumento=(codigo_pedido,fecha,usuario,total_compra)
    Db.modifica_db(sql,argumento)
    Cartel = f'''Usuario: {usuario} 
                Codigo de pedido: {codigo_pedido} 
                Total de la compra: {total_compra}'''
    return Cartel    

