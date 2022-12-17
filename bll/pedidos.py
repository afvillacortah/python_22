from dal.db import Db

def listar_pedidos(fecha):
    sql= 'SELECT * FROM "Pedidos" WHERE fecha=(?)'
    argumento = (fecha,)
    resp = Db.consulta_db(sql,False,argumento)
    return resp

def listar_fechas():
    sql = 'SELECT DISTINCT fecha FROM Pedidos'
    resp = Db.consulta_db(sql)
    return resp

def marcar_pedido_entregado(cod_pedido):
    sql = '''UPDATE Pedidos SET pendiente_entrega = ? 
         WHERE codigo = ? '''
    argumentos = (0,cod_pedido)
    Db.modifica_db(sql,argumentos)

def agregar_pedido(codigo_pedido,fecha,usuario,total_compra):
    sql = "INSERT INTO Pedidos VALUES (?,?,?,?,?)"
    argumento=(codigo_pedido,fecha,usuario,total_compra,1) #el campo pend_entrega es 1 (True) por defecto
    Db.modifica_db(sql,argumento)

#retorna el menor codigo valido para agregar un pedido a la tabla Pedidos
def obtener_codigo_compra():
    sql ="SELECT MAX(codigo)FROM 'Pedidos' "
    resp = Db.consulta_db(sql,True)
    if(resp[0] == None):
        resp = 1
        return(resp)
    else:
        resp = int(resp[0]) + 1
        return(resp) 