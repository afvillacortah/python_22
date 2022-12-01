#funciones y procedimientos que permiten  'CRUD' en la base de datos
import sqlite3
PATH = 'test.db'

class db:
    
    #CREAR TABLAS SI NO EXISTEN PARA usuarios,productos,administradores
    def crea_tabla_usuarios():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(30) PRIMARY KEY,
            password VARCHAR(50),email VARCHAR(30),cuit INTEGER(11),direccion VARCHAR (40) NOT NULL
            ,ciudad VARCHAR(15),provincia VARCHAR(),telefono INTEGER )""")
    
    def crea_tabla_administradores():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS administradores (nombre VARCHAR(30) PRIMARY KEY,
            password VARCHAR(50),email VARCHAR(30),cuit INTEGER(11),direccion VARCHAR (40) NOT NULL
            ,ciudad VARCHAR(15),provincia VARCHAR(20),telefono INTEGER )""")
    
    def crea_tabla_productos():
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS productos (id_producto INTEGER PRIMARY KEY
            AUTOINCREMENT ,nombre VARCHAR(30) NOT NULL,
            marca VARCHAR(50),precio REAL,stock INTEGER)""")
    


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
    def valida_cuenta(nombre,password,tabla):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            #mostrar datos de cada producto
            cursor.execute(f"""SELECT nombre FROM '{tabla}' WHERE nombre ='{nombre}' 
                       AND password = '{password}'""")
            resultado_busqueda= cursor.fetchall()
            if(len(resultado_busqueda) == 1):
                return True
            else:
                return False
    



    




