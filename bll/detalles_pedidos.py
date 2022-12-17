from dal.db import Db

def listar_detalle(codigo_pedido):
    sql='SELECT id,codigo_producto,producto,cantidad,precio_unitario,codigo_pedido FROM Detalle_pedidos WHERE codigo_pedido = (?)'
    argumento = (codigo_pedido,)
    resp = Db.consulta_db(sql,False,argumento)
    return resp
    
def agregar_detalle_compra(id,cod_prod,nombre,cantidad,precio_unit,cod_pedido):
    sql ="INSERT INTO Detalle_pedidos VALUES (?,?,?,?,?,?)"   
    '''id,codigo_producto,producto,cantidad,precio_unitario,codigo_pedido'''
    argumento =(id,cod_prod,nombre,cantidad,precio_unit,cod_pedido)
    Db.modifica_db(sql,argumento)

def obtener_codigo_inicial_detalle_pedidos():
    sql ="SELECT MAX(id) FROM 'Detalle_pedidos' "
    resp = Db.consulta_db(sql,True)
    if(resp[0] == None):
        resp = 1
        return(resp)
    else:
        resp = int(resp[0]) + 1
        return(resp) 