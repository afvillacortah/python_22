import sqlite3
from datetime import date
import hashlib
PATH = 'test.db'
#funciones y procedimientos que permiten  'CRUD' en la base de datos

class Db:
       
    #sirve para modificar alguna tabla recibe una consulta y opcionalmente una tupla con los parametros para la consulta
    #permite actualizar, crear tabla, eliminar y agregar algun elemento
    @staticmethod
    def modifica_db(consulta,parametros=()):
        with sqlite3.connect('TEST.DB') as conexion:
            cursor = conexion.cursor()
            if len(parametros) != 0 :
                cursor.execute(consulta,parametros)
            else:
                cursor.execute(consulta)
            conexion.commit()

    @staticmethod
    def modifica_db_varios(consulta,parametros=()):
        with sqlite3.connect('TEST.DB') as conexion:
            cursor = conexion.cursor()
            cursor.executemany(consulta,parametros)
            conexion.commit()
    
    @staticmethod
    #realiza una consulta con WHERE y si obtiene algun valor retorna true sino false 
    def busca_uno_varios(consulta,parametros):
        with sqlite3.connect('TEST.DB') as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta,parametros)
            resp = cursor.fetchall()
            if(len(resp) >0):
                return True
            else:
                return False
    
    #dal retornar los datos de la consulta en un mensaje
    def consulta_db(consulta,parametros=()):
        with sqlite3.connect('TEST.DB') as conexion:
            cursor = conexion.cursor()
            if len(parametros) != 0 :
                cursor.execute(consulta,parametros)
                resp = cursor.fetchall()
            return resp
            

    #CREAR TABLAS SI NO EXISTEN PARA usuarios,productos,administradores,reg. compras y ticket
    def crea_tabla_usuarios():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (id VARCHAR(30) PRIMARY KEY,
            password VARCHAR(50),email VARCHAR(30),cuit INTEGER(11),direccion VARCHAR (40) NOT NULL
            ,ciudad VARCHAR(15),provincia VARCHAR(),telefono INTEGER )""")
    
    def crea_tabla_administradores():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS administradores (id VARCHAR(30) PRIMARY KEY,
            password VARCHAR(50),email VARCHAR(30) )""")
    
    def crea_tabla_productos():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS productos (id INTEGER
            ,nombre VARCHAR(30) NOT NULL,
            marca VARCHAR(50),precio REAL,stock INTEGER,PRIMARY KEY(id_compra AUTOINCREMENT))""")

    
    def crea_tabla_registro_compras():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS registro_compras (id_compra INTEGER ,
            id_usuario VARCHAR(30),fecha VARCHAR,monto REAL,PRIMARY KEY(id_compra AUTOINCREMENT))""")
   
    def crea_tabla_ticket_compra():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS tickets_compras (id INTEGER ,
            producto VARCHAR(30),precio REAL,id_compra INTEGER,PRIMARY KEY(id AUTOINCREMENT),
            FOREIGN KEY(id_compra) REFERENCES registro_compras(id_compra) )""")

    def agregar_usuario(usuario):#usuario es una lista con los campos a agregar
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",usuario)
            conexion.commit()
    

    #indica si un nombre_usuario esta en una tabla especificada por parametro
    def pertenece_tabla(usr,tabla):
        with sqlite3.connect(PATH)as conexion:
            cursor = conexion.cursor()
            respuesta = cursor.execute(f"SELECT nombre FROM '{tabla}'usuarios WHERE nombre = '{usr}' ")
            if(respuesta.fetchone()!= None):
                return True # el usuario 'usr' esta en la tabla 'tabla'
            else:
                return False # el usuario 'usr' no esta en la tabla 'tabla'
    
    #buscar todos los producto cuyo nombre empiece por 'nombre' y tienen un stock mayor a 0 
    def buscar_producto(nombre):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            #mostrar datos de cada producto
            cursor.execute(f"""SELECT nombre,marca,precio,stock FROM productos WHERE nombre LIKE '{nombre}%' 
                       AND stock > 0""")
            resultado_busqueda= cursor.fetchall()
            for producto in resultado_busqueda:
                print(producto)
    
    #valida que usuario y password  pertenece a 'tabla'
    def valida_log_in(id,password,tabla):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            #mostrar datos de cada producto
            cursor.execute(f"""SELECT nombre FROM '{tabla}' WHERE nombre ='{id}' 
                       AND password = '{password}'""")
            resultado_busqueda= cursor.fetchall()
            if(len(resultado_busqueda) == 1):
                return True
            else:
                return False
    #valida que stock disponible para comprar
    def valida_stock(id_prod,cant_comprar):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute(f"""SELECT stock FROM productos WHERE id_producto = '{id_prod}' 
            AND stock > 0
            AND stock >= '{cant_comprar}' """)
            respuesta = cursor.fetchall()
            if(len(respuesta) == 1):
                return True
            else:
                return False
    #actualizar stock mermando la cantidad comprada
    def actualiza_stock_compra(id_prod,cant_compra):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute(f"""UPDATE productos SET stock = stock -'{cant_compra}'
             WHERE id_producto = '{id_prod}' """) 
    
    


