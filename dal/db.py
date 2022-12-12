import sqlite3
from datetime import date

PATH = 'Data_base.db'


class Db:
       
    #sirve para modificar alguna tabla recibe una consulta y opcionalmente una tupla con los parametros para la consulta
    #permite actualizar, crear tabla, eliminar y agregar algun elemento
    @staticmethod
    def modifica_db(consulta,parametros=()):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta,parametros)
            conexion.commit()

    @staticmethod
    def modifica_db_varios(consulta,parametros=()):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.executemany(consulta,parametros)
            conexion.commit()
    
    @staticmethod
    #realiza una consulta con WHERE y si obtiene algun valor retorna true sino false 
    def busca_uno_varios(consulta,parametros):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta,parametros)
            resp = cursor.fetchall()
            if(len(resp) > 0):
                return True
            else:
                return False
    
    #retornar los datos como una tupla
    @staticmethod
    def consulta_db(consulta,retorna_uno=False,parametros=()):
        with sqlite3.connect(PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta,parametros)
            if retorna_uno == False :
                resp = cursor.fetchall()
            else:
                resp = cursor.fetchone()
            return resp
            
    
    
    

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
    
    


