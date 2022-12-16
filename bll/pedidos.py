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