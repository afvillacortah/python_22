from dal.db import Db


def poblar_tablas():
    datos_roles = [(1,'administrador'),(2,'usuario'),(3,'vendedor')]
    consulta_roles = '''INSERT INTO "Roles" VALUES (?,?)'''
    consulta_cat_prod = '''INSERT INTO "Categorias_productos" VALUES (?,?)'''
    datos_cat_prod = [
    (1,'bebidas'),
    (2,'comestibles'),
    (3,'articulos de limpieza'),
    (4,'higiene personal'),
    (5,'bazar'),
    (6,'alimento para mascotas')]
   
    Db.modifica_db_varios(consulta_roles,datos_roles)
    Db.modifica_db_varios(consulta_cat_prod,datos_cat_prod)

def crea_tablas(): #tablas para guardar los datos de los usuarios
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
                        "fecha_nacimiento"	TEXT,"email"	TEXT NOT NULL,
                        "telefono"	REAL NOT NULL,"domicilio"	TEXT NOT NULL,
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
    

