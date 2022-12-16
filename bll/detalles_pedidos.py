from dal.db import Db

def listar_detalle(codigo_pedido):
    sql='SELECT producto,cantidad FROM Detalle_pedidos WHERE codigo_pedido = (?)'
    argumento = (codigo_pedido,)
    resp = Db.consulta_db(sql,False,argumento)
    lista_detalle =''
    for p,c in resp:
        if(p and c):
            lista_detalle += (f'{p}  \t  {c}  \n ' )
    return (lista_detalle)
    