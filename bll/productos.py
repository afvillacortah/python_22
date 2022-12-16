from dal.db import Db
def listar_stock(codigo):
    sql = 'SELECT "stock" FROM "Productos" WHERE "codigo" = (?);'
    arg = (codigo,)
    result = Db.consulta_db(sql,True,arg)
    return result