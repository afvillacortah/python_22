from dal.db import Db


def valida_nom_mar(variable):
    return (variable != "" and (not variable.isdigit()))
def valida_stock(stock):
    return (stock.isdigit() and stock != '0') 

#retorna un True si el producto no existe ya sino False
def valida_producto_no_existe(nombre,marca):
    sql = '''SELECT "codigo" FROM 'Productos'
                                 WHERE id = ?
                                AND marca = ?
                                '''
    argumento = (nombre,marca)
    return not(Db.busca_uno_varios(sql,argumento))

def valida_precio(precio):
    try:
        precio = float(precio)
        if(precio > 0):
            return True
    except:
        return False

def valida_categoria(categoria):
    return categoria != '0'

def valida_producto(nombre_producto,marca,stock,precio,categoria):
    return (valida_producto_no_existe(nombre_producto,marca) and valida_nom_mar(nombre_producto) and 
    valida_nom_mar(marca) and valida_stock(stock)and valida_precio(precio)and valida_categoria(categoria))

def valida_cod_nom_marca(codigo,nombre,marca):
    #la combinacion nombre/marca ya existe:
    #                             1- Cuando no se le cambia el nombre y la marca --> validacion True
    #                            2- Si al cambiar nombre y/o marca se encuentra duplicado con un codigo diferente-->validacion False
    #el producto no existe -->validacion True

    if (not(valida_producto_no_existe(nombre,marca))): #el producto como (nombre/marca) ya existe
        #si el producto no se le cambio los datos
        sql = 'SELECT codigo FROM Productos WHERE id = ? AND marca = ?'
        arg = (nombre,marca)
        resp = Db.consulta_db(sql,False,arg)
        retorna = True
        if len(resp)> 0:
            for r in resp:
                for c in r:
                    if(codigo != int(c)):
                        retorna = False
        else:
            retorna =True
    else:
        retorna = True
    return retorna

def valida_producto_actualizacion(codigo,nombre,marca,stock,precio):
    return (valida_cod_nom_marca(codigo,nombre,marca) and valida_nom_mar(nombre) and
    valida_nom_mar(marca) and valida_stock(stock)and valida_precio(precio))

def retornar_ultimo_id_producto(): #puede retornar un numero o 0 si la tabla es vacia
    sql ="SELECT MAX(codigo)FROM 'Productos' "
    resp = Db.consulta_db(sql,True)
    if(resp[0] == None):
        resp = 0
        return(resp)
    else:
        resp = int(resp[0])
        return(resp)
def agregar_producto(nombre,marca,stock,precio,categoria):
    codigo = retornar_ultimo_id_producto() + 1
    sql = '''INSERT INTO "Productos" VALUES (?,?,?,?,?,?,?)'''
    stock = int(stock)
    precio = float(precio)
    categoria = int(categoria)
    argumento = (codigo,nombre,marca,stock,precio,1,categoria)
    Db.modifica_db(sql,argumento)

def listar_productos(nombre):
    sql = f"""SELECT p.codigo,p.id,p.marca,p.stock,p.precio,p.categoria,c.categoria categoria
     FROM Productos p 
     INNER JOIN Categorias_productos c ON p.categoria = c.codigo
     WHERE p.id LIKE '%{nombre.lower()}%' OR p.id LIKE '%{nombre.capitalize()}%' ;"""
    resultado = Db.consulta_db(sql)
    return resultado
    

def obtener_producto(codigo):
    sql =f"""SELECT p.codigo,p.id,p.marca,p.stock,p.precio,p.es_activo,p.categoria,c.categoria categoria
     FROM Productos p 
     INNER JOIN Categorias_productos c ON p.categoria = c.codigo
     WHERE p.codigo = (?) ;"""
    
     
    argumento = (int(codigo) ,)
    return Db.consulta_db(sql,True,argumento)

def actualizar_producto(codigo,nombre,marca,stock,precio,estado,categoria):
    sql = f'''UPDATE Productos SET id = ? ,marca = ? ,stock = ?,precio = ?,es_activo = ?,categoria = ?
         WHERE codigo = {codigo} '''
    stock = int(stock)
    precio = float(precio)
    arg = (nombre,marca,stock,precio,estado,categoria)
    Db.modifica_db(sql,arg)

def obtener_detalle_compra(codigo_pedido):
    sql = 'SELECT * FROM Detalle_pedidos WHERE codigo_pedido =(?)'
    argum = (codigo_pedido,)
    return Db.consulta_db(sql,True,argum)
    