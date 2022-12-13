from dal.db import Db


def valida_nom_mar(variable):
    return (variable != "" and (not variable.isdigit()))
def valida_stock(stock):
    return (stock.isdigit() and stock != '0') 

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
    sql = '''INSERT INTO "Productos" VALUES (?,?,?,?,?,?)'''
    stock = int(stock)
    precio = float(precio)
    categoria = int(categoria)
    argumento = (codigo,nombre,marca,stock,precio,categoria)
    Db.modifica_db(sql,argumento)

def listar_productos(nombre):
    sql = f"""SELECT p.codigo,p.id,p.marca,p.stock,p.precio,p.categoria,c.categoria categoria
     FROM Productos p 
     INNER JOIN Categorias_productos c ON p.categoria = c.codigo
     WHERE p.id LIKE '%{nombre.lower()}%' OR p.id LIKE '%{nombre.capitalize()}%' ;"""
    resultado = Db.consulta_db(sql)
    return resultado
    